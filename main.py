import json
from datetime import datetime

current_time = datetime.now()
timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

def shelter():
    with open("shelter.json", "r", encoding="utf-8") as file: 
        shelter = json.load(file)
    print(f"Shelter Name: {shelter["shelter_name"]}")
    print(f"Leader: {shelter["leader"]}")
    print(f"Survivors: {shelter["survivors"]}")
    print(f"Food: {shelter["food"]}")
    print(f"Water: {shelter["water"]}")
    print(f"Baricade Health: {shelter["barricade_health"]}")
    if shelter["radio_working"] == True:
        print("Radio: Working.")
    else:
        print("Radio: Not working.")
    return shelter

def dumpshelter(info):
    with open("shelter.json", "w", encoding="utf-8") as file: 
        json.dump(info, file, indent=4)

def makechange(shelter):
    print("CURRENT SHELTER DATA")

    print(f"1. Shelter Name: {shelter["shelter_name"]}")
    print(f"2. Leader: {shelter["leader"]}")
    print(f"3. Survivors: {shelter["survivors"]}")
    print(f"4. Food: {shelter["food"]}")
    print(f"5. Water: {shelter["water"]}")
    print(f"6. Baricade Health: {shelter["barricade_health"]}")
    if shelter["radio_working"] == True:
        print("7. Radio: Working.")
    else:
        print("7. Radio: Not working.")
    loop = True
    while loop != False:
        try:
            user = int(input("Enter which one you'd like to change: "))
            if user not in [1,2,3,4,5,6,7]:
                raise ValueError("Out of range. (1 to 7)")
            else:
                loop = False
        except ValueError:
            print("ValueError - Must be a number answer (1-7)")
    

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

shelter1 = shelter()

loop = testforfile()
while loop != False:
    user = menu()
    if user == 4:
        loop = False
    elif user == 3:
        changesinfo = getchanges()
    elif user == 2:
        makechange(shelter1)
    elif user == 1:
        shelterinfo = shelter()
