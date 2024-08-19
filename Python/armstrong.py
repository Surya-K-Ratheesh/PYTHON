n = int(input("Enter a no.: "))

t = n
sum = 0

for i in range(t):
    sum = sum + (i*i*i)

if n == sum:
    print(n,"is an Armstrong no.")

else:
    print("Not an Armstrong no.")