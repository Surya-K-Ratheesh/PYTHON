from pack import * 

def main():
    a = int(input("Enter a no: "))
    b = int(input("Enter a no: "))
    
    print("1.Add \n2.Subtract \n3.Multiply \n.4.Divide")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        add(a,b)
        
    elif ch == 2:
        sub(a,b)
        
    elif ch == 3:
        multi(a,b)
        
    elif ch == 4:
        div(a,b)
        
    else:
        print("Enter a Valid Choice")
    
    
if __name__ == "__main__":
    main()