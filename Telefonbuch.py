import os

Telefonbuch = {"No Entries": ""}
try:
    geeky_file = open('Telefonbuch.txt', 'r')
    Data = geeky_file.read()
    geeky_file.close()
except:
    print("Unable to write to file")


def str_to_dict(string):
    string = string.strip('{}')
    string = string.strip("'")
    pairs = string.split(", ")
    return {key[0:]: value for key, value in (pair.split(': ') for pair in pairs)}

try:
    Telefonbuch = str_to_dict(Data)

except:
    print("")

def search_for_name():
    while True:
        global Search_name
        try:
            for p in Telefonbuch:
                if Search_name.lower() or Search_name.upper() in p:
                    print(p)
            break
        except:
            print("Thats a Number")
            continue
        break

def search_for_number():
    while True:
        global Search_Number
        try:
            for p in Telefonbuch.values():
                if Search_Number in p:
                    print(p)
            break
        except:
            print("You need a Number")
            continue
        break

def Save_to_File():
    Speicherdatei = str(Telefonbuch)
    try:
        geeky_file = open('Telefonbuch.txt', 'w')
        geeky_file.write(Speicherdatei.translate({ord("'"): None}))
        geeky_file.close()


    except:
        print("Unable to write to file")

def Name_input():
    global Name

    while True:
        Name = input("Enter a Name: ")
        if Name.isdigit():
            print("PLease type in a name not a number")
            continue
        else:
            break
    return Name

def Number_input():
    global Number

    while True:
        Number = input("Enter a Number: ")
        if not Number.isdigit():
            print("PLease type in a Number")
            continue
        else:
            break

    return Number


def telefonbuchoption():
    global Search_name
    global Search_Number
    while True:
        choice = input("\n\n\nChoose one of thes options\n1.New Entry\n2.List all\n3.Delete entry\n4.Search\n5.Stop\nEnter number here: ")

        if choice == str(1):
            print("\n\n")
            Name_input()
            Number_input()
            Telefonbuch[Name] = Number
            try:
                del Telefonbuch["No Entries"]
            except:
                print("")

            os.system('cls' if os.name == 'nt' else 'clear')
            print(Name +" is now saved in the list with the Number: " + Number)
            Save_to_File()
            continue

        elif choice == str(3):
            print("\n\n")
            Name_input()
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                del Telefonbuch[Name]
                print(Name + " got deleted from the list")
            except KeyError:
                print("This name is not on your list.")
            Save_to_File()
            continue

        elif choice == str(2):
            print("\n\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            for key, value in sorted(Telefonbuch.items()):
                print(key, value)
            if len(Telefonbuch) == 0:
                print("No Entries")
            continue

        elif choice == str(5):
            print("Exiting Programm...")
            break
        elif choice == str(4):
            print("\n\n")
            Search_name = input("Type in the Name you´r looking for: ")
            Search_Number = input("Type in the Number you´r looking for: ")
            print("\n\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            search_for_name()
            search_for_number()
        else:
            print("\n\n")
            print("That´s not an option.")
            continue

telefonbuchoption()
Speicherdatei = str(Telefonbuch)




