def main():
    # temp = []
    # count = 0
    # flag = 0
    
    # for i in range(1, 101):
    #     for j in range(2,i):
    #         if i % j == 0:
    #             flag = 1
    #             break
            
    #         else:
    #             flag = 0
            
    #     if (flag == 0):
    #         temp.append(i)
    #         count += 1
                    
    # print(f"No of prime no. b/w 1 to 100 is {count}")
    # for element in temp:
    #     print(element,end=',')
        
    # print(" ")
    
    temp = []
    count  = 0
    flag = 0
    
    i = 1
    while(i <= 101):
        j = 2
        
        while(j < i):
            if i % j == 0:
                flag = 1
                break
                
            j += 1
                
        if flag == 0:
            temp.append(i)
            count += 1
            
        i += 1
        
    print(f"No of prime no. b/w 1 to 100 is {count}")
    for element in temp:
        print(element,end=',')
        
    print(" ")
    
    
        
                   
if __name__ == "__main__":
    main()