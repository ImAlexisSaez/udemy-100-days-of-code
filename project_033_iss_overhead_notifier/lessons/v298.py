import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
# data_position = data["iss_position"]
data_longitude = data["iss_position"]["longitude"]
data_latitude = data["iss_position"]["latitude"]

iss_position = (data_longitude, data_latitude)
print(iss_position)
