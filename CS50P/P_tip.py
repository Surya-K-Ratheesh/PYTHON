def main():
    dollars = dollar_to_float(input("Enter price of your dish: "))

    percent = percent_to_float(input("Enter tip percent: "))

    tip = dollars * percent

    print(f"Tip is {tip:.2f}")


def dollar_to_float(d):
    d = d.removeprefix('$')
    d = float(d)
    return d

def percent_to_float(p):
    p = p.removesuffix('%')
    p = float(p)
    p = p/100
    return(p)

main()