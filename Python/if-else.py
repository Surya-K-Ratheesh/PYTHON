age = int(input("Enter age: "))

if age >= 18:
    print("Adult")

elif age < 18 and age > 12:
    print("Child")

else:
    print("Infants")