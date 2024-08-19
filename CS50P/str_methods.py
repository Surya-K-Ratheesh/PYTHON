#Imput name
name = input("Hi! Whats your name: ").strip().title()


print(f"Hello, {name}")

"""
#Remove white spaces from String
name = name.strip()


#Capitalize users name
name = name.capitalize() #1st Letter is capitalized


#Capitalize 1st letter of each word
name = name.title()
"""
#OR

#name = name.strip().title()


#Say Hello
print(f"Hello, {name}")


#Splitting users name into first middle and last

first, middle, last = name.split()
print(f"Hello, {first}")
print(f"Hello, {last}")