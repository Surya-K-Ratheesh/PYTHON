def main():
    while True:
        try:
            x = int(input("Enter 1st no: "))
            y = int(input("Enter 2nd no: "))
            break
            
        except ValueError:
            print("Enter 2 numbers")
            
        except (IndexError, EOFError):
            pass
        

     
    ch =  input("Select operation: [+, -, *, /, %, **]: ")

    if (ch == '+'):
        print(f"Sum of {x} and {y} =", sum(x,y))

    elif (ch == '-'):
        print(f"Difference of {x} and {y} =", dif(x,y))

    elif (ch == '*'):
        print(f"Product of {x} and {y} =", pro(x,y))

    elif (ch == '/'):
        print(f"Quotient of {x} and {y} =", quo(x,y))

    elif (ch == '%'):
        print(f"Remainder of {x} and {y} =", rem(x,y))

    elif (ch == '**'):
        print(f"{x} raised to the power {y} =", pow(x,y))

    else:
        print("Choose a valid Operator")
        
    

def sum(a,b):
    return a + b 

def dif(a,b):
    return a - b

def pro(a,b):
    return a * b

def quo(a,b):
    return a / b

def rem(a,b):
    return a % b

def pow(a,b):
    po = round(a ** b)
    return po


if __name__ == "__main__":
    main()