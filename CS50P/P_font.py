import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    randomFont = True
    
elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    randomFont = False
    
else:
    sys.exit(1)
    
figlet.getFonts()

if randomFont == False:
    try:
        figlet.setFont(font=sys.argv[2])
        
    except:
        print("Invalid Input")
        sys.exit(1)
        
else:
    font = random.choice(figlet.getFonts())
    
msg = input("Input: ")

print("Output: ")
print(figlet.renderText(msg))