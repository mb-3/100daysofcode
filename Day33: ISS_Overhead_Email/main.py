import requests
from datetime import datetime
import smtplib
import time as t

MY_LAT = ######
MY_LNG = ######
my_email = "mjb.python@gmail.com"
password = ""


def is_iss_close():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_position = (iss_longitude, iss_latitude)

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LNG - 5 < iss_longitude < MY_LNG + 5:
        return True


def is_dark():
    parameters = {
        # "lat": MY_LAT,
        # "lng": MY_LNG,
        "formatted": 0,
    }
    srss_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    srss_response.raise_for_status()

    srss_data = srss_response.json()
    sunrise = int(srss_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(srss_data["results"]["sunset"].split("T")[1].split(":")[0])

    if time_hour > sunset or time_hour < sunrise:
        return True


while True:

    t.sleep(60)
    time = datetime.now()
    time_hour = time.hour
    if is_dark() and is_iss_close():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:ISS\n\nLook up!!!!"
            )
