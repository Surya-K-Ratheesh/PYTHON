#Find the sum of 1+(1+2)+(1+2+3)+.....(1+2+.....+n) Using a single while loop

n = int(input("Enter a no "))
sum = 0
i = 0
temp = 0

while i <= n:
    temp += i
    sum += temp
    i += 1
    
print(f"Sum = {sum}")
    