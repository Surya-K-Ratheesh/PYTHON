sfname = input("Enter the file name: ")
sdata = input("Enter the content / 'exit' to terminate: ")

fp = open(sfname,'w')

while sdata != 'exit':
    fp.write(sdata)
    fp.write('\n')
    sdata = input('')

    
fp.close()