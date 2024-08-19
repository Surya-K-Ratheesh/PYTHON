"""
for i in range:
    perform task
"""
"""
for i in [0, 1, 2]:  # List
    print("Meow")
"""

"""
for _ in range(3):
    print("Meow")
    
print(" ")

print("Meow \n" * 3, end = ' ')
"""

"""
n = int(input("Enter a no: "))

for _ in range(n):     #Range takes a numeric value
    print("Meow")
"""

def main():
    x = get_no()
    
    meow(x)
    
def get_no():
    while True:
        n = int(input("Enter a no:"))
        if n > 0:
            return n
    
def meow(n):
    for _  in range(n):
        print("Meow")
        
main()