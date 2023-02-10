import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # Response code 200 (Success)
print(response.status_code)
