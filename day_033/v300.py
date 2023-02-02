import requests
from datetime import datetime


# Data for: Alhambra (Web: https://www.latlong.net/)
ALHAMBRA_LATITUDE = 37.176010
ALHAMBRA_LONGITUDE = -3.588670

parameters = {
    "lat": ALHAMBRA_LATITUDE,
    "lng": ALHAMBRA_LONGITUDE,
    "formatted": 0,
}

response = requests.get(
    url="https://api.sunrise-sunset.org/json",
    params=parameters,
)
response.raise_for_status()

data = response.json()

sunrise_hour = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hour = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now().hour



