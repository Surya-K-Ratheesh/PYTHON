from collections import Counter


order = []

while True:
    try:
        item = input("").strip().title()

    except EOFError:
        break
    
    order.append(item)

print("\nORDER")

item_count = Counter(order)

sort = sorted(item_count.keys())

for item in sort:
    count = item_count[item]
    print(f"{count} {item.upper()}")


