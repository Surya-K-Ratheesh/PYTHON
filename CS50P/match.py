name = input("Whats Your Name: ")

"""
match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
"""


def main():
    time = input("What time is it? ")

    hours, minutes = time.split(':')

    convert(time)

    breakfast_start = 7
    breakfast_end = 8
    lunch_start = 12
    lunch_end = 13
    dinner_start = 18
    dinner_end = 19

    if breakfast_start <= hours < lunch_start:
        print("Breakfast Time")

    elif lunch_start <= hours < dinner_start:
        print("Lunch Time")

    elif dinner_start <= hours <= dinner_end:
        print("Dinner Time")

    else:
        print("Invalid Time entered")


def convert(time):
    hours = int(hours)
    minutes = int(minutes)

    return hours, minutes