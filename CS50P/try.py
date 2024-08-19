def main():
    x = get_int("Whats x?: ")
    print(f"Value of x = {x}")   



def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            
        except ValueError:                   # ValueError - Type of error when the user enters a value which is not of the specified data type.
            #print("x is not an integer")
            pass
            
        #else:
            #break
        
 
main()   
        
# Here 'else' is associated with 'except'.