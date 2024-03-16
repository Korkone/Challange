import os

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

Telefonbuch = str_to_dict(Data)

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
    while True:
        choice = input("\n\n\nChoose one of thes options\n1.New Entry\n2.List all\n3.Delete entry\n4.Stop\nEnter number here: ")

        if choice == str(1):
            print("\n\n")
            Name_input()
            Number_input()
            Telefonbuch[Name] = Number
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
            for key, value in Telefonbuch.items():
                print(key, value)
            continue

        elif choice == str(4):
            break
        else:
            print("\n\n")
            print("That´s not an option.")
            continue

telefonbuchoption()
Speicherdatei = str(Telefonbuch)

