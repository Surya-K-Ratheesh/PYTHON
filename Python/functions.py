#INBUILT FUNCTIONS 
int()
str()
bool()

#MODILE FUNCTIONS
import math
#print(dir(math))

from math import *
print(sqrt(9))

#USER DEFINED
    # def function_name(parameters):
    #   perform task

def print_sum(num1,num2=7): # sum2=7 - Setting as backup if no number is entered for num2
    print(num1 + num2)

print_sum(7,9)