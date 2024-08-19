#1. two numbers are given check whether one is a factor of other

a = int(input("Enter a no: "))
b = int(input("Enter a no: "))


if a % b == 0:
    print(f"{b} is a factor of {a}")
    
else:
    print(f"NO Match")
    
    