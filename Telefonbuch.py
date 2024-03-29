import os
import random

vornamen_liste = ["", "Peter", "Andreas", "Max", "Paul", "Hanno", "Sascha", "Pascal", "Veronika", "Lisa", "Brigitte", "Sebille", "Anne", "Hanna", "Susanne"]
nachnamen_liste = ["","Schmit", "Petersen", "sodeh", "Reiter", "Fugi", "Sesala", "Pismana", "Hauser", "Beloni"]
count = 0
Telefonbuch = {"No Entries": "0"}
try:
    file = open('Telefonbuch.txt', 'r')
    Data = file.read()
    file.close()
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
print(Telefonbuch)
def Searching_options():
    global Search_Number
    global Search_name
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\n")
        search_choice = input(
            "Search options are the following\n1.Search Name\n2.Search Number\n3.Search Name and Number\n4.Back to Menu\nPlease choose one option: ")
        if search_choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            Search_name = input("\nType in the Name you´r looking for: ")
            print("Here are the Results of your Name Search")
            search_for_name()
            break

        elif search_choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            Search_Number = input("\nType in the Number you´r looking for: ")
            print("\nHere are the Results of your Number Search")
            search_for_number()
            break

        elif search_choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            Search_name = input("\nType in the Name you´r looking for: ")
            Search_Number = input("\nType in the Number you´r looking for: ")
            print("\nHere are the Results of your Name Search")
            search_for_name()
            print("\nHere are the Results of your Number Search")
            search_for_number()
            break

        elif search_choice == "4":
            break

        else:
            print("\nSorry this is not an Option")
            continue

def search_for_name():
    while True:
        global Search_name
        global count
        count = 0
        try:
            for p in Telefonbuch:
                if Search_name.lower() in p or Search_name.upper() in p:
                    count += 1
                    print (str(count) +". " + p +": " + Telefonbuch[p])
                    if p == "":
                        print("No entry found")
            break
        except:
            print("Thats a Number")
            continue
        break

def search_for_number():
    while True:
        global Search_Number
        global count
        count = 0
        try:
            for p in Telefonbuch.values():
                if Search_Number in p:
                    count += 1
                    print(str(count) +". " + list(Telefonbuch.keys())[list(Telefonbuch.values()).index(p)]+ ": " + (p))
                    if p == "  ":
                        return "No Entries"
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
        choice = input("\n\nChoose one of thes options\n1.New Entry\n2.List all\n3.Delete entry\n4.Search\n5.Add a Random Entry\n6.Stop\nEnter number here: ")

        if choice == str(1):
            print("\n\n")
            Name_input()
            Number_input()
            Telefonbuch[Name] = Number
            try:
                del Telefonbuch["No Entries"]
                Save_to_File()
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

            continue

        elif choice == str(6):
            print("\nExiting Programm...")
            break
        elif choice == str(4):
            Searching_options()

        elif choice == str(5):
            print("\n\n")
            os.system('cls' if os.name == 'nt' else 'clear')
            Telefonbuch[vornamen_liste[random.randint(1,14)]+" " +nachnamen_liste[random.randint(1,9)]] = random.randint(218,359)
            print("a Random name and number got addet to your entrie list")
            Save_to_File()
            continue

        else:
            print("\n\n")
            print("That´s not an option.")
            continue

telefonbuchoption()
Save_to_File()




