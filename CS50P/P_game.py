import random
import sys


while True:
    try:
        level = int(input("Level: "))
        
        num = random.randint(1, level)
        
        while True:
            guess = int(input("Guess: "))

            if num == guess:
                print("Just Right")
                sys.exit()
                
            elif num > guess:
                print("Too small")
                
            else:
                print("Too large")
        
    except ValueError:
        pass
    
    except EOFError:
        break

