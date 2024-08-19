def main():
    list = [1,5,4,3,2,6,7]
    
    target = 6
    
    two_sum(list,target)
    

def two_sum(list,target):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if(list[1] + list[j] == target):
                return i, j
    

if __name__ == '__main__':
    main()  