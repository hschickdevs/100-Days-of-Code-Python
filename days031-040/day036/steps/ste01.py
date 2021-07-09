import os
import requests

STOCK = "TSLA"

params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.getenv('ALPHA_KEY')
}

response = requests.get('https://www.alphavantage.co/query', params=params).json()["Time Series (Daily)"]
data = [value for value in response.values()]

yesterday_value = float(data[0]['4. close'])
before_yesterday_value = float(data[1]['4. close'])

percentage = (yesterday_value - before_yesterday_value) * 100 / yesterday_value

if not (-0.01 <= percentage <= 0.01):
    print("Get News")
