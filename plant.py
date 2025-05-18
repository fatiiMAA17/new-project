import json
from datetime import datetime
import time

plants = []


def help_menu():
  print("""
Help - Instructions:
0. Help: See this menu.
1. Add Plant: Add a new plant with its care info.
2. View Plants: See all saved plant records.
3. Search: Find a plant by ID or name.
4. Update: Modify any plant's info.
5. Delete: Remove a plant.
6. Summary: See average watering frequency.
7. Save: Save data to a file.
8. Load: Load data from a file.
9. Clear: Delete all plant data.
10. Exit: Quit the app.
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
            print("Invalid input, try again.")

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
            print(f"ID{p['id']} - {p['name']} ({p['type']}), every {p['watering_frequency']} days, date of last watering: {p['last_watered']}")
            print(f"Your additional note: {p['additional_note']})

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
            p["watering_frequency"] = get_input("New frequency: ", int)
            p["last_watered"] = get_date("New date (YYYY-MM-DD): ")
            print("Updated.")
            return
    print("Not found.")

def delete():
    pid = get_input("ID to delete: ", int)
    for p in plants:
        if p["id"] == pid:
            plants.remove(p)
            print("Deleted.")
            return
    print("Not found.")

def sum_stat():
    if not plants:
        print("No data.")
        return
    total = len(plants)
    avg = sum(p["watering_frequency"] for p in plants) / total
    print(f"{total} plants. Avg frequency: {avg:.1f} days")

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
        with open("plants.json", "r") as f:
            plants = json.load(f)
        print("Loaded.")
    except:
        print("Could not load file.")

def clear():
    c = input("Clear all data? (y/n): ")
    if c.lower() == "y":
        plants.clear()
        print("Data cleared.")

def menu():
    while True:
        print("\n🌿 Plant Care Scheduler Menu:")
        print("""
0. Help Menu
1. Add Plant
2. View all Plant
3. Search Plant
4. Update Plant
5. Delete Plant
6. Summary Statistics
7. Save to file
8. Load from file
9. Clear All Data
10. Exit
        """)
        c = get_input("Select option: ", int)
        if c == 0: help_menu()
        elif c == 1: add()
        elif c == 2: view()
        elif c == 3: find()
        elif c == 4: update()
        elif c == 5: delete()
        elif c == 6: sum_stat()
        elif c == 7: save()
        elif c == 8: load()
        elif c == 9: clear()
        elif c == 10:
            print(" Goodbye!!! ")
            break
        else:
            print("Invalid.")
        wait()

start()
menu()