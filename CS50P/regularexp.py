import re

"""
. - any character except a newline
* - 0 or more repetitions
+ - 1 or more repetitions
? - 0 or 1 repetitions
{m} - m repetitions
{m,n} - m-n repetitions
^ - Matches the start of the string
$ - Matches the end of the string just b4 the newline at the end of the string.
[] - Set of characters - Characters that must be there
[^] - Complementing the set - Characters that must not be there

\w - Word charcters as well as numbers and underscore
\W - Not a word character
\d - Decimal digit
\D - Not a decimal digit
\s - Whitespace character
\S - Not a whitespace character 

A|B - either A or B
(...) - Group
(?:...) - Non-capturing version

re.search(pattern, string, flags=0)
re.IGNORECASE
re.MULTILINE
re.DOTALL
"""

email = input("Whats your email: ").strip()

"""
if "@" in email and "." in email:
    print("Valid")
    
else:
    print("Invalid")
"""

"""
username, domain = email.split("@")


if username and domain.endswith(".com"):
    print("Valid")
    
else:
    print("Invalid")
"""


"""
if re.search(".+@.+", email):
    print("Valid")
    
else:
    print("Invalid")
"""

"""
if re.search(r"^.+@.+\.com$",email):  # Raw string - In this case it is used to take '\' as it is and not for newline '\n'. 
    print("Valid") # Adding ^ and $ indicates where to look for - My email is "7suryakr@gmail.com" - only looks at the gmail address and leaves the rest.
    
else:
    print("Invalid")
"""    
    
"""    
if re.search(r"^[^@].+@[^@].+\.com$",email): # [^@] it says - anything except '@' sign, used to check repetition of @
    print("Valid") 
    
else:
    print("Invalid")
"""    
 
"""   
if re.search(r"^[a-zA-Z0-9_].+@[a-zA-Z0-9_].+\.com$",email): 
    print("Valid") 
    
else:
    print("Invalid")
"""
    
if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|org|gov|in)$",email, re.IGNORECASE): #Uppercase email is also considered
    print("Valid") # (...) - Group  ? - 0 or 1 rep  (\w+\.) - indicates      
    
else:
    print("Invalid")