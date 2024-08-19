str = input("Input:")

new_str = ""

for char in str:
    if char not in "aeiouAEIOU":
        new_str += char

print(new_str)