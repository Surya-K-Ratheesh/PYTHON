def main():
    count = 0
    flag = 0
    odd = 0
    even = 0
    
    for i in range (2,101):
        for j in range (2,i):
            if i % j == 0:
                flag = 1
                break
            
            else:
                flag = 0
                
        if flag == 0:
            count += 1
            
            if i % 2 == 0:
                print(f"{i} is Even")
                even += 1
                    
                    
            else:
                print(f"{i} is Odd")
                odd += 1
                    
                    
    print(f"No of prime no b/w 2 and 100 is {count}")
    print(f"No of Odd prime no b/w 2 and 100 is {odd}")
    print(f"No of Even prime no b/w 2 and 100 is {even}")


if __name__ == '__main__':
    main()
    
    
"""
def main():
    temp = []
    even = 0
    odd = 0
    count = 0
    flag = 0
    
    for i in range(1, 101):
        for j in range(2,i):
            if i % j == 0:
                flag = 1
                break
            
            else:
                flag = 0
            
        if (flag == 0):
            temp.append(i)
            count += 1
            
            if (i % 2 == 0):
                even += 1
                
            else:
                odd += 1
                    
    print(f"No of prime no. b/w 1 to 100 is {count}")
    print(f"No of Even prime no. b/w 1 to 100 is {even}")
    print(f"No of Odd prime no. b/w 1 to 100 is {odd}")
    
    for element in temp:
        print(element,end=',')
        
    print(" ")
        
                   
if __name__ == "__main__":
    main()
"""