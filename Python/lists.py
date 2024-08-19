marks = [44, 44.5, 48, 30, 24]
print(marks)
print(marks[0])
print(marks[-1])
print(marks[0:2]) #Does not include ending index
print(marks[1:3])

# 44 44.5 48 30 24
#  0  1   2   3  4
# -5 -4  -3  -2  -1


for score in marks:
    print(score) 


marks.append(50) #Add something in the end
print(marks)

marks.insert(3 , 43) #insert(index , subject)
print(marks)

marks.remove(48)
print(marks)

print(43 in marks)

print(len(marks))

print(" ")

i = 0

while i < len(marks):
    print(marks[i])
    i += 1

marks.clear() #Empty List
print(marks)