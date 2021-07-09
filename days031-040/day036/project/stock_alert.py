import os
import requests

from twilio.rest import Client


def gen_message(stock, title, description, percentage):
    if percentage < 0:
        emoji = '🔻'
    else:
        emoji = '🔺'
    return f'{stock}: {emoji}{abs(percentage)}%\nHeadline:{title}\nBrief:{description}'


STOCK = "TSLA"
COMPANY_NAME = "Tesla"

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.getenv('ALPHA_KEY'),
    'language': 'en'
}

response = requests.get('https://www.alphavantage.co/query', params=params).json()["Time Series (Daily)"]
data = [(key, value) for key, value in response.items()]

yesterday_value = float(data[0][1]['4. close'])
before_yesterday_value = float(data[1][1]['4. close'])

round_percentage = round((yesterday_value - before_yesterday_value) * 100 / yesterday_value)
if not (-5 <= round_percentage <= 5):
    params = {
        'qInTitle': COMPANY_NAME,
        'apiKey': os.getenv('NEWS_KEY'),
        'language': 'en'
    }
    response = requests.get('https://newsapi.org/v2/everything', params=params).json()
    top_3 = response['articles'][:3]
    all_news = [{'headline': article['title'], 'brief': article['description']} for article in top_3]

    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    phone_number = os.environ['TWILIO_NUMBER']
    my_number = os.environ['MY_NUMBER']

    client = Client(account_sid, auth_token)
    for news in all_news:
        message = client.messages.create(
            body=gen_message(STOCK, news['headline'], news['brief'], round_percentage),
            from_=phone_number,
            to=my_number)
        print(message.status)
    

