import json
from datetime import datetime

current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

def shelter():
    with open("shelter.json", "r", encoding="utf-8") as file: 
        shelter = json.load(file)
    print(f"Shelter name: {shelter["shelter_name"]}")
    print(f": {shelter["shelter_name"]}")

def dumpshelter(info):
    with open("shelter.json", "w", encoding="utf-8") as file: 
        json.dump(info, file, indent=4)

def changes(change):
    entry = f"{timestamp} | {change}" 
    with open("changes.log", "a", encoding="utf-8") as file: 
        file.write(entry + "\n")


def getchanges():
    try:
        with open("changes.log", "r", encoding="utf-8") as file: 
            changes_text = file.read() 
        if changes_text.strip(): 
            print(changes_text) 
        else: 
            print("There have been no changes.") 
    except FileNotFoundError: 
        print("No change entries have been saved yet.")

def menu():
    print("Zombie Shelter Manager")
    print("1. View shelter information")
    print("2. Change a shelter value")
    print("3. View change log")
    print("4. Quit")
    loop = True
    while loop != False:
        try:
            user = int(input("Enter your choice: "))
            if user not in [1,2,3,4]:
                raise ValueError("Out of range. (1 to 4)")
            else:
                loop = False
        except ValueError:
            print("ValueError - Must be a number answer (1-4)")
    return user

def testforfile():
    try:
        with open("shelter.json", "r", encoding="utf-8") as file: 
            shelter_text = file.read()
        return True
    except FileNotFoundError:
        print("JSON file, 'shelter.json' missing.")
        return False



loop = testforfile()
while loop != False:
    user = menu()
    if user == 4:
        loop = False
    elif user == 3:
        changesinfo = getchanges()
    elif user == 2:
        print("")
    elif user == 1:
        shelterinfo = shelter()
