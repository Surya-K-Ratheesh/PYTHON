"""
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")
    
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] #tuple - Here name and class in returned together as one set
"""


