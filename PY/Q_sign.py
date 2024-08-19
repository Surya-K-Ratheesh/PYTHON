# A no. is given, check whether its +ve -ve or zero

a = int(input("Enter a no: "))

"""
if (a == 0):
    print("ZERO")
    
elif (a > 0):
    print(f"{a} is Positive")
    
else:
    print(f"{a} is Negative")
"""

if a > 0:
    print(f"{a} is Positive")
elif a < 0:
    print(f"{a} is Negative")
    
else:
    print("ZERO")