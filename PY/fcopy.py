sfname = input("Enter the source file name: ")

dfname = input("Enter the destination file name: ")

fpr = open(sfname,'r')
fpw = open(dfname,'w')

fpw.write(fpr.read())

fpr.close()
fpw.close()
