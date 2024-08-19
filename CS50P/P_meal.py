def main():
    #Enter time from User
    time =  input("What time is it? ")

    #Convert to float
    user_hours = convert(time)


    #Define Time Range
    breakfast_start = 7.0
    breakfast_end = 8.0
    lunch_start = 12.0
    lunch_end = 13.0
    dinner_start = 18.0
    dinner_end = 19.0

    #Checking entered time against time ranges
    if breakfast_start <= user_hours < lunch_start:
        print("Breakfast Time")

    elif lunch_start <= user_hours < dinner_start:
        print("Lunch Time")

    elif dinner_start <= user_hours <= dinner_end:
        print("Dinner Time")

    else:
        print("Invalid Time entered")

def convert(time_str):
    #Split time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))

    #Calculate Total hours including minutes as fraction of hours
    total_hours = hours + minutes / 60

    return total_hours

if __name__ == "__main__":
    main()