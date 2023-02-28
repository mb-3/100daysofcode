import requests
import pandas
import os
from twilio.rest import Client

my_phone = os.environ.get("MY_PHONE_NUM")
STOCK = "AMZN"
COMPANY_NAME = "Amazon"
up_icon = "🔺"
down_icon = "🔻"

account_sid = "ACc78f4dd09ba2d02039fd2150c4ec95eb"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY_AUTH")
NEWS_PARAMETERS = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "qInTitle": COMPANY_NAME,
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY_AUTH")
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}

# Stock API
stock_response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
print(f"Stock status_code: {stock_response.status_code}")
stock_raw_data = stock_response.json()
df = stock_raw_data['Time Series (Daily)']

# News API
news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
print(f"News status_code: {news_response.status_code}")
news_raw_data = news_response.json()
news_article_list = news_raw_data['articles'][:3]

# Stock Data
df_list = [i for i in list(df.items())[:2]]
close_list = [(item, float(stock_dict['4. close'])) for item, stock_dict in df_list]

yesterday_close = close_list[0][1]
dby_close = close_list[1][1]

close_price_diff = abs(round(yesterday_close - dby_close, 2))
alert_threshold = round(close_list[0][1] * .05, 2)
stock_percent_delta = round((close_price_diff / yesterday_close) * 100, 2)

if yesterday_close > dby_close:
    is_up = True
else:
    is_up = False

if is_up:
    stock_direction = up_icon
else:
    stock_direction = down_icon

if close_price_diff >= alert_threshold:
    client = Client(account_sid, auth_token)
    for i in news_article_list:
        message = client.messages \
            .create(
            body=f"{STOCK}: {stock_direction}{stock_percent_delta}%\n"
                 f"Headline: {i['title']}\n"
                 f"Brief: {i['description']}",
            from_='+18445820504',
            to=f"+1{my_phone}"
        )

        print(message.status)
else:
    print(f"The price difference of {close_price_diff} does not exceed the threshold of {alert_threshold}. "
          f"No messages sent.")
