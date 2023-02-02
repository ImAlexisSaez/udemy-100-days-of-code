import requests
import smtplib
import time
from datetime import datetime

# Mail settings
MY_EMAIL = "test@gmail.com"
PASSWORD = "1234"

# Data for: Alhambra (Web: https://www.latlong.net/)
ALHAMBRA_LATITUDE = 37.176010
ALHAMBRA_LONGITUDE = -3.588670


def is_iss_over_alhambra():
    # Get the ISS position
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    return abs(iss_latitude - ALHAMBRA_LATITUDE) <= 5 and abs(iss_longitude - ALHAMBRA_LONGITUDE) <= 5


def is_night():
    # Get the sunset data for Alhambra
    parameters = {
        "lat": ALHAMBRA_LATITUDE,
        "lng": ALHAMBRA_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return not (sunrise < time_now < sunset)


while True:
    if is_iss_over_alhambra() and is_night():
        # Send mail
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=MY_EMAIL, password=PASSWORD)  # Login details
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:ISS!\n\nLook up!"
            )
    time.sleep(60)  # Check every minute
