import csv


while True:
    try:
        name = input("Enter name: ")
        home = input("Enter Home: ")
        
        with open("stud.csv", "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "home"]) # fieldnames are the order in the values are to be entered (It as hint for DictWriter )
            writer.writerow({"name" : name, "home" : home})
    except EOFError:
        break
        