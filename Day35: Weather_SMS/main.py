import requests
import os
from twilio.rest import Client

account_sid = 'ACc78f4dd09ba2d02039fd2150c4ec95eb'
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
my_phone = os.environ.get("PHONE_NUM")
END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
LAT = 41.032730
LON = -73.766327

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
}
response = requests.get(END_POINT, params=parameters)
print(response.status_code)
df = response.json()
df_list = df['list']


for i in range(0, 4):
    df_item = df_list[i]
    if df_item['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, bring an umbrella.",
        from_='+18445820504',
        to=my_phone
    )

    print(message.status)
