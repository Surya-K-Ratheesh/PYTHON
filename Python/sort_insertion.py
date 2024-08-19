def main():
    list = []
    n = int(input("Enter size of the array: "))
    
    for i in range(n):
        item = int(input("Enter elements: "))
        list.append(item)
        
    print("\nBEFORE SORTING")
    for i in range(n):
        print(list[i],end=", ")
    
        
    for i in range (n-1):
        small = i
        
        for j in range(i+1, n):
            if(list[j] < list[small]):
                small = j
                
        list[small],list[i] = list[i],list[small]
                
    print("\nAFTER SORING")
    for i in range(n):
        print(list[i],end=", ")
        
    print(" ")
            
        
if __name__ == '__main__':
    main()