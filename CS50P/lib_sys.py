import sys

"""
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    

print(f"Hello, my name is {sys.argv[1]}")
"""


#python3 lib_sys.py Surya
#python3 lib_sys.py "Surya K Ratheesh"

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
    
for arg in sys.argv[1:]:
    print(arg)

