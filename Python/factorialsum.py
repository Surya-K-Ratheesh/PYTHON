def main():
    n = int(input("Enter a no: "))
    
    sum = 0
    i = n
    # print(sum)
    
    while(i != n+2):
        
        pro = 1
        
        j = i
        while(j > 0):
            pro = pro * j
            # print(pro)
            
            j -= 1
            
        sum += pro
        
        i += 1
        
    print(sum)
        
    
if __name__ == '__main__':
    main()