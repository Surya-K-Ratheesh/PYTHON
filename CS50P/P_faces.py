#Main funtion
def main():
    str = input("Enter a string: ") #Entering a string

    #Function Call
    convert(str)

#Funtion Definition
def convert(str):
    str =  str.replace(':)','🙂').replace(':(','🙁') #----------- str.replace(old,new[, count])
    print(str)


main()