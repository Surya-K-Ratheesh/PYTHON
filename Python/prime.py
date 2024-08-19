def main():
    n = int(input("Enter a no: "))
    
    flag = 0
    
    for i in range(2,n):
        if n % i == 0:
            flag = 1
            break
        
    
    if flag == 0:
        print(f"{n} is a Prime no.")
        
    else:
        print(f"{n} is a consonent")
    
    
    
if __name__ == "__main__":
    main()