import csv

with open("df.csv",'w') as fp:
    fp.write("name,age")
    fp.write("\n")
    fp.write("abcd,20")
    fp.write("\n")
    fp.write("cda,30")
    fp.write("\n")
    fp.write("ggg,25")
    
fp.close()