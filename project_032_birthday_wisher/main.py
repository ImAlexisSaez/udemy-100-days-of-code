import datetime as dt
import pandas as pd
import random
import smtplib

# Mail settings
my_email = "test@gmail.com"
password = "1234"

# Get today's date
today = (dt.datetime.now().month, dt.datetime.now().day)

# Read the data
birthdays = pd.read_csv("birthdays.csv")

# Create a dictionary of birthdays
birthdays_dict = {
    (row.month, row.day): row for (index, row) in birthdays.iterrows()
}

# Check if today matches a birthday in the birthdays.csv
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter = file.read()
        letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  # Login details
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy birthday!\n\n{letter}"
        )
