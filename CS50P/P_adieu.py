import inflect

p = inflect.engine()

#A list to keep track of names
names = []


#Entering names from user (ctrl + D to stop)
while True:
    try:
        name = input("Name: ")
        names.append(name)
        
    except EOFError:
        print()
        break
    
    
output = p.join(names)
print("Adieu, adieu, to", output)

        
        
        