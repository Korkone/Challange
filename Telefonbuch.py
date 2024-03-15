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

print(Telefonbuch)
def telefonbuchoption():
    while True:
        choice = input("Choose one of thes options New Entry / list all / delete entry/Stop: ")

        if choice == "New Entry":
            New_Name = input("Add Name: ")
            New_Number = input("Add Number: ")
            Telefonbuch[New_Name] = New_Number
            continue

        elif choice == "delete entry":
            Del_Name = input("Waht name do you wana Delete?: ")
            del Telefonbuch[Del_Name]

        elif choice == "list all":
            print(Telefonbuch)
            continue

        elif choice == "Stop":
            break

        else:
            continue

telefonbuchoption()
Speicherdatei = str(Telefonbuch)

try:
    geeky_file = open('Telefonbuch.txt', 'w')
    geeky_file.write(Speicherdatei.translate({ord("'"): None}))
    geeky_file.close()


except:
    print("Unable to write to file")