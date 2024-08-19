#Find the sum of 1st n numbers using while loop

n = int(input("Enter a no: "))
sum = 0
i = 0

while i <= n:
    sum += i
    i += 1
    
print(f"Sum = {sum}")