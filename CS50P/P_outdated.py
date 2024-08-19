#Create a list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    #Take input from user
    date = input("Date: ").capitalize().strip()
    
    try:
        #split the entered date by /
        month, day, year = date.split('/')
        month = int(month)
        day = int(day)
        year = int(year)
        
        #Check if month is between 1 and 12 and day is between 1 and 31
        if 1<= day <=31 and 1<= month <= 12:
            break
        
    except:
        try:
            #split the date by space
            old_month, old_day, year = date.split(" ")
            
            #Finding the number of the month
            for i in range(len(months)):
                if old_month == months[i]:
                    month = i + 1
                    
            #remove comma from day variable
            day = old_day.replace(",","")
            
            month = int(month)
            day = int(day)
            year = int(year)
            
            #Check if month is between 1 and 12 and day is between 1 and 31
            if 1<= day <=31 and 1<= month <= 12:
                break
            
        except:
            print()
            pass
        

print(f"{year}-{month:02}-{day:02}")

    
            
            