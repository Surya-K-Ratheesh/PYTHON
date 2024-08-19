def main():
    count = 0
    flag = 0
    odd = 0
    even = 0
    
    i = 2
    
    while (i != 101):
        j = 2
        while (j != i):
            if i % j == 0:
                flag = 1
                break
            
            else:
                flag = 0
                
            j += 1
                
        if flag == 0:
            count += 1
            
            if i % 2 == 0:
                print(f"{i} is Even")
                even += 1
                    
                    
            else:
                print(f"{i} is Odd")
                odd += 1
                
        i += 1
                    
                    
    print(f"No of prime no b/w 2 and 100 is {count}")
    print(f"No of Odd prime no b/w 2 and 100 is {odd}")
    print(f"No of Even prime no b/w 2 and 100 is {even}")


if __name__ == '__main__':
    main()