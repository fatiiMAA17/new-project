import json
import os
from datetime import datetime
import time

plants = []

def help_menu():
    print("""
Help - Instructions:
1. Add Plant: Add a new plant with its care info.
2. View Plants: See all saved plant records.
3. Search: Find a plant by ID or name.
4. Update: Modify any plant's info.
5. Delete: Remove a plant.
6. Summary: See average watering frequency.
7. Save: Save data to a file.
8. Load: Load data from a file.
9. Clear: Delete all plant data.
10. Sort: Sort plants by any field.
11. Count: Count plants using recursion.
12. Help: See this menu.
13. Exit: Quit the app.
    """)

def start():
    print(r"""
          Welcome to Malikova Fatima's Plant Care Scheduler!
                        Let's grow together!
      """)
    time.sleep(2)

def wait():
    input("Press Enter to continue...")

def get_input(prompt, type_=str):
    while True:
        try:
            return type_(input(prompt))
        except:
            print(f"Invalid input, please enter a valid {type_.__name__}.")

def get_date(prompt):
    while True:
        date = input(prompt)
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except:
            print("Use YYYY-MM-DD format.")

def next_id():
    if not plants:
        return 1
    return max(p['id'] for p in plants) + 1

def add():
    print("Add a new plant")
    p = {
        "id": next_id(),
        "name": input("Plant Name: "),
        "type": input("Type of Plant: "),
        "watering_frequency": get_input("Watering (days): ", int),
        "additional_note": input("Make your additional note: "),
        "last_watered": get_date("Last watered (YYYY-MM-DD): ")
    }
    plants.append(p)
    print("Plant added.")

def view():
    if not plants:
        print("No plants found.")
    else:
        for p in plants:
            print(f"ID {p['id']} - {p['name']} ({p['type']}), every {p['watering_frequency']} days, last watered on {p['last_watered']}")
            print(f"Note: {p['additional_note']}")

def find():
    k = input("Search name or ID: ")
    for p in plants:
        if k.lower() in p['name'].lower() or str(p['id']) == k:
            print(p)
            return
    print("Not found.")

def update():
    pid = get_input("ID to update: ", int)
    for p in plants:
        if p["id"] == pid:
            p["name"] = input("New name: ")
            p["type"] = input("New type: ")
            p["watering_frequency"] = get_input("New frequency (days): ", int)
            p["last_watered"] = get_date("New last watered date (YYYY-MM-DD): ")
            p["additional_note"] = input("New additional note: ")
            print("Updated.")
            return
    print("Not found.")

def delete():
    pid = get_input("ID to delete: ", int)
    for p in plants:
        if p["id"] == pid:
            plants.remove(p)
            print("Deleted.")
            save() 
            return
    print("Not found.")

def sum_stat():
    if not plants:
        print("No data.")
        return
    total = len(plants)
    avg = sum(p["watering_frequency"] for p in plants) / total
    print(f"{total} plants. Avg watering frequency: {avg:.1f} days")

def save():
    try:
        with open("plants.json", "w") as f:
            json.dump(plants, f)
        print("Saved.")
    except:
        print("Error saving.")

def load():
    global plants
    try:
        if os.path.exists("plants.json"):
            with open("plants.json", "r", encoding="utf-8") as f:
                plants = json.load(f)
            print("Loaded.")
            view()  
        else:
            print("plants.json not found. Please save first.")
    except json.JSONDecodeError:
        print("File is empty or contains invalid JSON.")
    except Exception as e:
        print(f"Error loading file: {e}")

def clear():
    c = input("Clear all data? (y/n): ")
    if c.lower() == "y":
        plants.clear()
        print("Data cleared.")

def sort():
    field = input("Sort by (name/type/watering_frequency): ").lower()
    if field not in ["name", "type", "watering_frequency"]:
        print("Invalid field for sorting.")
        return
    sorted_plants = sorted(plants, key=lambda x: x[field])
    for p in sorted_plants:
        print(p)

def count(data):
    if not data:
        return 0
    return 1 + count(data[1:])

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n Plant Care Scheduler Menu:")
        print("""
1. Add Plant
2. View all Plants
3. Search Plant
4. Update Plant
5. Delete Plant
6. Summary Statistics
7. Save to file
8. Load from file
9. Clear All Data
10. Sort Plants
11. Count Plants (Recursively)
12. Help Menu
13. Exit
        """)
        c = get_input("Select option: ", int)
        if c == 1: add()
        elif c == 2: view()
        elif c == 3: find()
        elif c == 4: update()
        elif c == 5: delete()
        elif c == 6: sum_stat()
        elif c == 7: save()
        elif c == 8: load()
        elif c == 9: clear()
        elif c == 10: sort()
        elif c == 11: print(f"Total number of plants: {count(plants)}")
        elif c == 12: help_menu()
        elif c == 13:
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
        wait()

start()
menu()
