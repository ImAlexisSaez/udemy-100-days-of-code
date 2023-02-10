import os
import requests
from twilio.rest import Client

# OWM_API_KEY = "309598bae6bcdee8354457876324530c"
OWM_API_KEY = "69f04e4613056b159c2761a9d9e664d2"
# OWM_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
ELCHE_LAT = 38.267210
ELCHE_LNG = -0.695220

# Twilio
ACCOUNT_SID = "test"
AUTH_TOKEN = "test"

owm_api_parameters = {
    "lat": ELCHE_LAT,
    "lon": ELCHE_LNG,
    "appid": OWM_API_KEY,
    "lang": "es",
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWM_ENDPOINT, params=owm_api_parameters)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Hello",
        from="000111222333",
        to="999888777"
    )
    print(message.status)


