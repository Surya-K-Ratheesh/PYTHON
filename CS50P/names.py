"""
names = []

for _ in range(3):
    names.append(input("What's your name: "))
    
for name in sorted(names):
    print(f"Hello, {name}")
"""


# name = input("Hi, What's your name: ")


#Used to add names to the file
"""
file = open("names.txt", "a") # a - append
file.write(f"{name} \n")
file.close()
"""


# when using with keyword, we dont have to close a file. It automatically closes the file
"""
with open("names.txt", "a") as file:
    file.write(f"{name} \n")
"""


#Displaying the names in the file
"""
with open("names.txt" , "r") as file:  # r - read which is default
    lines = file.readlines()
    
for line in lines:
    #print("Hello", line, end = "")
    print("Hello,", line.rstrip())
"""
"""
with open("names.txt","r") as file:
    for line in file:
        print("Hello,",line.rstrip())
"""

#Sorting the file before printing

#sorted(iterable, /, *, key=None, reverse=False)


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names, reverse=True):
    print(f"Hello, {name}")

"""
with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,",line.rstrip())
"""