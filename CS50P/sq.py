def main():
    n = int(input("Enter side: "))
    
    square(n)
    
def square(size):
    #For each row in square
    for i in range(size):
        
        #For each brick in row
        for j  in range(size):
            
            #Print brick
            print("#", end = "")
            
        #Takes cursor to next line
        print()
        
main()