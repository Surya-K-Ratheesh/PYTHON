import csv

for i in range(3):
    name = input("Whats Your name: ")
    home = input("Wheres your home: ")

    with open("stu.csv" , "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, home])