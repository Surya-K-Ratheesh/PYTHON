def main():
    list = []
    n = int(input("Enter the no. of elements in list: "))
    
    for i in range(n):
        item = int(input(f"Enter Element {i+1}: "))
        list.append(item)
        
    print("\n")
    print("LIST BEFORE SORTING")
    for i in range(n):
        print(list[i], end = ", ")
        
    for i in range(n-1):
        for j in range(i+1, n):
            if (list[i] > list[j]):
                list[i],list[j] = list[j],list[i]
                
        
    print("\n")        
    print("LIST AFTER SORTING")
    for i in range(n):
        print(list[i], end =", ")
        
    print(" ")
    


if __name__ == '__main__':
    main()