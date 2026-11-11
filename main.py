import json
from datetime import datetime

try:
    with open("shelter.json", "r", encoding="utf-8") as file: 
        shelter1 = json.load(file)
    loop = True
except FileNotFoundError:
    print("JSON file, 'shelter.json' missing.")
    loop = False

current_time = datetime.now()
timestamp = current_time.strftime("%m-%d-%Y %H:%M:%S")

def shelter():
    print(f"Shelter Name: {shelter1["shelter_name"]}")
    print(f"Leader: {shelter1["leader"]}")
    print(f"Survivors: {shelter1["survivors"]}")
    print(f"Food: {shelter1["food"]}")
    print(f"Water: {shelter1["water"]}")
    print(f"Baricade Health: {shelter1["barricade_health"]}")
    if shelter1["radio_working"] == True:
        print("Radio: Working.")
    else:
        print("Radio: Not working.")

def dumpshelter(info):
    with open("shelter.json", "w", encoding="utf-8") as file: 
        json.dump(info, file, indent=4)

def makechange(shelter_data:dict):
    print("CURRENT SHELTER DATA")

    print(f"1. Shelter Name: {shelter_data["shelter_name"]}")
    print(f"2. Leader: {shelter_data["leader"]}")
    print(f"3. Survivors: {shelter_data["survivors"]}")
    print(f"4. Food: {shelter_data["food"]}")
    print(f"5. Water: {shelter_data["water"]}")
    print(f"6. Baricade Health: {shelter_data["barricade_health"]}")
    if shelter_data["radio_working"] == True:
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
    if user == 1:
        prev = shelter_data.get("shelter_name")
        chose = "shelter_name"
    elif user == 2:
        prev = shelter_data.get("leader")
        chose = "leader"
    elif user == 3:
        prev = shelter_data.get("survivors")
        chose = "survivors"
    elif user == 4:
        prev = shelter_data.get("food")
        chose = "food"
    elif user == 5:
        prev = shelter_data.get("water")
        chose = "water"
    elif user == 6:
        prev = shelter_data.get("barricade_health")
        chose = "barricade_health"
    elif user == 7:
        if shelter_data.get("radio_working") == True:
            prev = "Working"
        else:
            prev = "Not working"
        chose = "radio_working"

    user = None
    loop = True
    while loop != False:
        try:
            if chose == "shelter_name":
                user = input("Choose a new name for the shelter: ")
            elif chose == "leader":
                user = input("Choose a new name for the new leader: ")
            elif chose == "survivors":
                user = int(input("How many survivors are here?: "))
            elif chose == "food":
                user = int(input("How much food is left?: "))
            elif chose == "water":
                user = int(input("How much water is left?: "))
            elif chose == "barricade_health":
                user = int(input("How much health does the barricade have?: "))
            elif chose == "radio_working":
                user = str(input("Is the radio working? (Yes/y or No/n): "))

                if user.lower() in ["yes","y"]:
                    user = True
                elif user.lower() in ["no","n"]:
                    user = False
                elif user not in ["yes","y","no","n"]:
                    raise ValueError("Invalid choice. (No/n or Yes/y)")
            else:
                raise ValueError("Invalid choice.")
                
        except ValueError:
            print("Invalid")
            loop = True
        except AttributeError:
            print("Invalid")
            loop = True
        
        loop = False

    shelter_data.update({chose: user})

    if user == True:
        user = "Working."
    if user == False:
        user = "Not working."

    if user != prev:
        print(f"Previous: {prev}")
        print(f"Current: {shelter_data[chose]}")
        dumpshelter(shelter_data)
        changes(f"{chose} was changed to {user}")
    else:
        print("No changes have been made.")
    

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
