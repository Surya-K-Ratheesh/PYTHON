sfname = input("Enter a file name: ")

fp = open(sfname,'r')

for i in fp:
    print(i)
    
fp.close()