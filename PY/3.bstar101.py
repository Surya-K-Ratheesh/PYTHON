n = int(input("Enter a no: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("1" if (i+j) % 2 == 0 else "0", end = ' ')
    print()