"""
while(Condition):
    perform task
"""

"""
i = 3
while i != 0:
    print("Meow")
    i -= 1            # i - i - 1
"""

while True:
    n = int(input("Whats n?"))
    if n > 0:
        break
    
for _ in range(n):
    print("Meow")