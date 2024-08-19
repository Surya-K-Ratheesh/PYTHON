# Insert a string into a list and check for the occurance of each letter and print the count.

def main():
    str = input("Enter a string: ")
    lis = list(str)
    temp = [] 
    
    print(lis)

    for i in lis:
        if i not in temp:
            count = 0
            for j in lis:
                if i == j:
                    count += 1
                    
            temp.append(i)        
            print(f"No. of occurance of {i} = {count}")
        
         
        

if __name__ == "__main__":
    main()
            
