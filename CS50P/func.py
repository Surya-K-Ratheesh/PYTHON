"""
def hello(to = "World"):
    print(f"Hello {to}")

hello()
name = input("Hi! What's your name?: ")
hello(name)
"""

def main():
    hello()
    name = input("Hi! What's your name?: ")
    hello(name)

def hello(x = "World"):
    print(f"Hello {x}")


main()