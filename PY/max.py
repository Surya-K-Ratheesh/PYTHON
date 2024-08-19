a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
c = int(input("Enter 3rd no: "))

"""
if a < b and a < c:
    print(f"minimum is {a}")
elif b < a and b < c:
    print(f"minimum is {b}")
else:
    print(f"minimum is {c}")
"""
"""
if a < b:
    if a < c:
        print(f"Minimum = {a}")
        
    else:
        print(f"Minimum = {c}")
        
else:
    if b < c:
        print(f"Minimum = {b}")
        
    else:
        print(f"Minimum = {c}")
"""

if a < b:
    m = a
    
else:
    m = b
    
if c < m:
    m = c
    
print(m)