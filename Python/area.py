#Pgm to find the area 

print("Select any one - 'Square' , 'Rectangle' , 'Circle'")

a = input("s - square, r - rectangle, c - circle: ")

def arsq(a):
    ar = s * s
    print("Area of square of side",s,"=",ar)

def arec(a,b):
    are = a * b
    print("Area of rectangle =",are)

def arcir(a):
    area = 3.14*a*a
    print("Area of circle of radius",a,"=",area)


    
if a == 's':
    s = int(input("Enter side"))
    arsq(s)
    

elif a == 'r':
    l = int(input("Enter Length: "))
    b = int(input("Enter Breadth: "))
    arec(l,b)
    

elif a == 'c':
    r = int(input("Enter Radius: "))
    arcir(r)
    

else:
    print("Enter a valid option")

