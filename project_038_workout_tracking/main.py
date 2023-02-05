import datetime as dt
import os
import requests
from requests.auth import HTTPBasicAuth

# Personal data:
GENDER = "male"
WEIGHT = 100
HEIGHT = 186
AGE = 42

# Data for Nutritionix.com:
NUTRITIONIX_APP_ID = os.environ["NUTRITIONIX_APP_ID"]
NUTRITIONIX_APP_KEY = os.environ["NUTRITIONIX_APP_KEY"]

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

EXERCISE_HEADERS = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

# Sheety authorization:
SHEETY_POST_ENDPOINT = os.environ["SHEETY_POST_ENDPOINT"]
SHEETY_USER = os.environ["SHEETY_USER"]
SHEETY_PASS = os.environ["SHEETY_PASS"]
sheety_basic_auth = HTTPBasicAuth(SHEETY_USER, SHEETY_PASS)

# Ask for exercises
exercise_query = input("What exercise did you do today? ")

exercise_params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(
    url=EXERCISE_ENDPOINT,
    json=exercise_params,
    headers=EXERCISE_HEADERS,
)
exercises_data = response.json()
exercises_list = exercises_data["exercises"]

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in exercises_list:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": round(exercise["duration_min"], 0),
            "calories": round(exercise["nf_calories"], 0),
        }
    }

    sheet_response = requests.post(url=SHEETY_POST_ENDPOINT, json=sheet_inputs, auth=sheety_basic_auth)

    print(sheet_response.text)
