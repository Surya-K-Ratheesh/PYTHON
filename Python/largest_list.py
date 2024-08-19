def main():
    n = int(input("Enter size of list: "))
    list = [n]
    
    print("Enter the elements in list: ")
    for i in range(0,n):
        item = int(input("Enter no: "))
        list.append(item)
        
    temp = list[0]
        
    for i in range(0, n):
        if list[i] > temp:
            temp = list[i]
            
    
    print(f"The largest element in the list is {temp}")
    
    
    
if __name__ == "__main__":
    main()