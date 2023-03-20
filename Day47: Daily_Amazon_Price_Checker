import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

deal_price = 20.00

my_email = os.environ['MY_EMAIL']
pw = os.environ['PW']

url = "https://camelcamelcamel.com/product/B08149FMTG"
header = {
    "User-Agent": os.environ['USER-AGENT'],
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url=url, headers=header)
data = response.text

soup = BeautifulSoup(data, "lxml")

item_price = float(soup.find(class_="green").getText().strip("$"))
item_name = soup.select(selector="h2 a")[0].getText()
item_link = soup.find(name="div", class_="column small-12").find(name="a")['href']

if item_price <= deal_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"The Amazon Product:\n{item_name} is now a deal at {item_price}!\nGet it here: {item_link}",
        )
