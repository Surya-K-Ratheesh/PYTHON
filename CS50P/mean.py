import statistics

marks = []


n = int(input("Enter Size: "))
    
    
for i in range(n):
    num = int(input("Enter numbers: "))
    marks.append(num)
    
    
print(statistics.mean(marks))
    
