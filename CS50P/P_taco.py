menu ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

order = []
total_cost = 0.00

print("To stop press (ctrl + D)") 

while True:
    try:
        item = input("Item: ").strip().title()
    except EOFError:
        break
    
    if item in menu:
        order.append(item)
        total_cost += menu[item]
        print(menu[item])
        
    else:
        print("Invalid Item")
        
print("\nThank You for your order",end = '\n \n')
print("Your total order is")

for item in order:
    print(item)
    
print(f"Total Cost = {total_cost:.2f}")
