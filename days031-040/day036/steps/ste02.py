import os
import requests

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

percentage = (yesterday_value - before_yesterday_value) * 100 / yesterday_value

if not (-0.01 <= percentage <= 0.01):
    params = {
        'qInTitle': COMPANY_NAME,
        'apiKey': os.getenv('NEWS_KEY'),
        'language': 'en'
    }
    response = requests.get('https://newsapi.org/v2/everything', params=params).json()
    top_3 = response['articles'][:3]
    print(top_3)

