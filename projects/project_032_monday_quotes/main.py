import datetime as dt
import random
import smtplib

# Mail settings
my_email = "test@gmail.com"
password = "1234"

# Check the day
current_week_day = dt.datetime.now().weekday()

# Send the mail on Mondays:
if current_week_day == 0:
    # Read data
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()

    # Select random quote:
    random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  # Login details
        connection.sendmail(
            from_addr=my_email,
            to_addrs="destinatary@gmail.com",
            msg=f"Subject:Motivational quote\n\n{random_quote}"
        )
