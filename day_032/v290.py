import datetime as dt

now = dt.datetime.now()

year = now.year

day_of_week = now.weekday()

if year == 2020:
    print("Wear a facemask!")

print(day_of_week)

# Create a date
date_of_birth = dt.datetime(year=1980, month=9, day=25)
print(date_of_birth)
