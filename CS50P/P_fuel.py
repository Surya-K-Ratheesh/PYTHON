while True:
    try:
        fraction = input("Fraction: ")

        x, y = fraction.split('/')
        x = int(x)
        y = int(y)



    except (ValueError, ZeroDivisionError):
        pass

    else:
        break

percent = (x/y)*100

if percent <= 1:
    print("E")

elif percent >= 99:
    print("F")

elif percent == 25.0:
    print("25%")

elif percent == 50.0:
    print("50%")

elif percent == 75.0:
    print("75%")

else:
    print("")
