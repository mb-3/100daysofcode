import requests
import os
import datetime as dt

today = dt.datetime.now()
username = os.environ.get("USERNAME_AUTH")
token = os.environ.get("PIXELA_TOKEN_AUTH")
quantity = ""
headers = {
    "X-USER-TOKEN": token
}


# ----------------------------- USER CREATE ----------------------------- #

pixela_endpoint = "https://pixe.la/v1/users"
pixela_parameters = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=pixela_parameters)
# print(response.text)


# ----------------------------- GRAPH CREATE ----------------------------- #

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "kuro",
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)


# ----------------------------- PIXEL CREATE ----------------------------- #

pixel_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_parameters['id']}"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": quantity,
}

# response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)
# print(response.text)


# ----------------------------- PIXEL UPDATE ----------------------------- #

pixel_update_endpoint = f"{pixel_endpoint}/{pixel_parameters['date']}"
update_parameters = {
    "quantity": quantity
}

# response = requests.put(url=pixel_update_endpoint, json=update_parameters, headers=headers)
# print(response.text)
