 # This import the correct things related to dates and times, neccessary for anything to do with dates or times
from datetime import datetime, date, time


# Getting curent date and storing in variable
today = date.today()
#By default, printing a date will show it in the format YYYY-MM-DD
print(today)

tomorrow = date(2026, 1, 21) # This date format is called ISO format
print(tomorrow)  # Prints 2026-01-21

# You can create a date from string format using the isoformat method
next_week = date.fromisoformat("2026-01-28")
print(next_week)

right_now = datetime.now()  # This gets the current date and time
print(right_now)

print(right_now.timestamp()) # using timestamp method to get number of seconds since epoch

my_date = datetime.fromtimestamp(1700000000) # Creating a datetime object from a timestamp
print(my_date)