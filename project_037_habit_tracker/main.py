import datetime as dt
import requests

USERNAME = "alexissaez"
USER_TOKEN = "87g8e7rt78nkm!-456"
CODING_GRAPH_ID = "coding-time"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USER_PARAMS = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create a user account:
# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)

# Create a graph definition:
# graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_params = {
#     "id": "coding-time",
#     "name": "Coding Graph Time",
#     "unit": "min",
#     "type": "int",
#     "color": "shibafu",
# }
#
headers = {
    "X-USER-TOKEN": USER_TOKEN,
}
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)

# Post a value to the graph:
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{CODING_GRAPH_ID}"

today = dt.datetime(year=2023, month=2, day=4)

# response = requests.post(
#     url=pixel_endpoint,
#     json={
#         "date": today.strftime("%Y%m%d"),
#         "quantity": "185",
#     },
#     headers=headers,
# )

pixel_put_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{CODING_GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.put(
#     url=pixel_put_endpoint,
#     json={
#         "quantity": "125",
#     },
#     headers=headers,
# )
# print(response.text)

pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{CODING_GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.delete(
    url=pixel_delete_endpoint,
    headers=headers,
)
print(response.text)