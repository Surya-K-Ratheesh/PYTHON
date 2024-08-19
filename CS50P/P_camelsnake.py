def main():
    camel = input("camelcase: ")
    
    snake = cameltosnake(camel)
    
    print(snake)
    
def cameltosnake(camel):
    #declaring a variable to store the changes.
    snakec = ""
    
    #For checking every alphabet in string.
    for char in camel:
        
        #Checking if the alphabet is uppercase or not.
        if char.isupper():
            
            #if the character is in uppercase - change it to lower case and also add a "_" in front.
            snakec += "_" + char.lower()
        
        #if already in lowercase - add it to snakec.   
        else:
            snakec += char
            
    if snakec.startswith("_"):
        snakec = snakec[1:]
        
    return snakec 

main()