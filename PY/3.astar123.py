"""
1
12
123
1234
Atleast in 2 different logics
"""


n = int(input("Enter a no: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end = ' ')
    print()