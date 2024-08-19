def main():
    n = int(input("Enter the no. of elements: "))
    list = []
    
    for i in range(n):
        item  = int(input("Enter Elements: "))
        list.append(item)
        
    first = 0
    last = n
    mid = int((first + last)/2)
    
    for j in range(0,mid):
        for i in range(mid-1):
            for k in range(i+1, mid):
                if (list[i] > list[k]):
                    list[i],list[k] = list[k],list[i]
    
    for j in range(mid,n):
        for i in range(mid,n):
            for k in range(i+1, n):
                if (list[i] > list[k]):
                    list[i],list[k] = list[k],list[i]
    
    for i in range(n):
        for k in range(i+1, n):
            if (list[i] > list[k]):
                list[i],list[k] = list[k],list[i]
                    
    print(list)
        
    
if __name__ == '__main__':
    main()