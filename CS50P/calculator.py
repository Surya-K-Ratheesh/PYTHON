x = float(input("Enter 1st no: "))
y = float(input("Enter 2nd no: "))

ch = input("Choose an operator: [+, -, /, *, %]: ")

if (ch == '+'):
    sum = x + y
    print(f"Sum of {x} and {y} = {sum:,}", sep=' = ')

elif (ch == '-'):
    dif = x - y
    print(f"Difference of {x} and {y} =", dif)

elif (ch == '*'):
    pro = x * y
    print(f"Product of {x} and {y} = {pro:.2f}")

elif (ch == '/'):
    quo = round(x/y,2) # ----------------------------  round(number[,ndigits])
    print(f"Quotient of {x} and {y} = {quo}")

elif (ch == '%'):
    print(f"Remainder of {x} and {y} =", x%y)

else:
    print("Choose a valid operator") 