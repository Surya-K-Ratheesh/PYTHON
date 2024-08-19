import csv

with open("df.csv",'r') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    lc = 0
    for row in csv_reader:
        if lc == 0:
            print("".join(row))
            #print(lc,"\n")
            lc += 1
            
        else:
            print("".join(row))
            #print(lc,"\n")
            lc += 1
    