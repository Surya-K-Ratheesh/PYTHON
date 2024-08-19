sfname = input("Enter the file name: ")

fp = open(sfname,'r')

print(fp.read())

fp.close()