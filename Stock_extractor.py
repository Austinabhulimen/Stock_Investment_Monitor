import requests
from twilio.rest import Client

# FOR STOCK_API
stock_api_key = "78YXDL5U9T1FOP2X"
Twilio_API_KEY = "352d62048a18bb7075cb2cba123bbd9e"

account_sid ="AC46a495e287d80cf65af5e104d4b61f8c"
account_token="b53aa8d26734de5d34be9ede115b8f4a"

parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":"TSLA",
    "interval":"Daily",
    "apikey":stock_api_key,

}

# FOR NEWS_API

parameters_news= {
    "apiKey":"36b17800f4c5427fb8a6565c595f1b96",
    "q":"tesla",
    "from":"2021-04-12",
    "sortBy":"publishedAt",


}





response = requests.get("https://www.alphavantage.co/query?",params=parameters)
response.raise_for_status()
result = response.json()["Meta Data"]
result2 = response.json()["Time Series (Daily)"]
print(result)
print("================")
print(result2)

day = response.json()["Time Series (Daily)"]
closing_price_previous_day = float(response.json()["Time Series (Daily)"]["2021-04-09"]["4. close"])
closing_price_next_day = float(response.json()["Time Series (Daily)"]["2021-04-12"]["4. close"])
print(f"for previous_day             closing price    {closing_price_previous_day}")
print(f"for the next_day             closing price    {closing_price_next_day}")

price_difference = abs(closing_price_next_day) - closing_price_previous_day
print(f"Here's the price difference               {price_difference}")

percentage = round((price_difference/closing_price_next_day)*100,2)


if percentage>3:
    parameters_news = {
        "apiKey": "36b17800f4c5427fb8a6565c595f1b96",
        "q": "tesla",
        "from": "2021-04-12",
        "sortBy": "publishedAt",

    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=parameters_news)

    result2 = response.json()["articles"][10]["title"]
    result3 = response.json()["articles"][10]["description"]
    final_result =f"title:{result2} \n, news {result3} \n"
    print(final_result)

    client = Client(account_sid, account_token)
    message = client.messages \
        .create(
        body=final_result,
        from_='+17042702798',
        to='+13136526912'

    )

    print(message.status)

else:
    print(f"Tesla made a {percentage} loss")