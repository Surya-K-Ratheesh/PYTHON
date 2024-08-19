#Calculator

first = int(input("Enter the 1st no.: "))
second = int(input("Enter 2nd no.: "))

print("Select required operation(+,-,*,/,%,**): ")
operator = input("Enter Operator: ")

if operator == '+':
    sum = first + second
    print("The Sum of",first,"&",second,"=",sum)

elif operator == '-': 
    dif = first-second
    print("The Difference of",first,"&",second,"=", dif)

elif operator == '*':
    pro = first*second
    print("The Product of",first,"&",second,"=", pro)

elif operator == '/':
    quo = first/second
    print("The Quotient of",first,"&",second,"=", quo)

elif operator == '%':
    mod = first%second
    print("The remainder of",first,"&",second,"=", mod)

elif operator == '**':
    pow = first**second
    print(first,"raised to the power",second,"=",pow)

else:
    print("Enter valid operator")