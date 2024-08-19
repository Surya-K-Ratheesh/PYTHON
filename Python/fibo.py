#Generate a fibonacci series and find the sum of odd and even terms seperately.
def main():
    n = int(input("Enter the no of terms: "))
    
    even = 0
    odd = 2
    
    i = 1
    a = 1
    b = 1
    
    print(a, b,end=" ")
    while(i != n-1):
        
        c = a + b
        
        if(c % 2 == 0):
            even += c
            
        else:
            odd += c
        
        print(c,end=" ")
        
        a = b
        b = c
        
        i += 1
    
    print("\n")    
    print(f"Sum of even terms = {even}")
    print(f"Sum of odd terms = {odd}")

        
if __name__ == '__main__':
    main()