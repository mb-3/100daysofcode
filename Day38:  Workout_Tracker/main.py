import requests
import datetime as dt
import os

today_date = dt.datetime.now().strftime("%m/%d/%Y")
today_time = dt.datetime.now().strftime("%H:%M")

# Nutri Info
NUTRI_APP_ID = os.environ["NUTRI_APP_ID"]
NUTRI_APP_KEY = os.environ["NUTRI_APP_KEY"]
query = input("Tell me which exercises you did: ")
nutri_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_APP_KEY,
}
nutri_parameters = {
    "query": query,
    "gender": "male",
    "weight_kg": 77,
    "height_cm": 180,
    "age": 27,
}
nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

response = requests.post(url=nutri_endpoint, json=nutri_parameters, headers=nutri_headers)
print(response.status_code)
workout_list = response.json()['exercises']

# Sheety Info
sheety_endpoint = os.environ["SHEETY_ENDPOINT"]
sheety_headers = {
    "Authorization": os.environ["SHEETY_AUTH"]
}

# Post Request
for i in workout_list:
    sheety_parameters = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": i['name'].title(),
            "duration": str(round(i['duration_min'])) + "min",
            "calories": i['nf_calories'],
        }
    }
    response = requests.post(url=sheety_endpoint, json=sheety_parameters, headers=sheety_headers)
    print(response.status_code)
