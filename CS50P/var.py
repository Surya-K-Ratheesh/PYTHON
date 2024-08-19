#Ask user for their name : COMMENT
name = input("Hi! Whats Your Name: ")

print("Hello" + name) #Concatenation
print("Hello", name)


#print(*objects, sep = '', end = '\n', file = sys.stdout, flush = False)

print("Hello", end = '')
print(name)

print("Hello", end = '!@!@!')
print(name)

print("Hello", name, sep="121")


#Printing quotes

print("Hello \"friend\"")
print('Hello "friend"')