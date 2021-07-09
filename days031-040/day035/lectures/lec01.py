import os
import requests

LATITUDE = 51.507351
LONGITUDE = -0.127758

api_key = os.getenv('OWM_KEY')

params = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'exclude': 'current,minutely,daily,alerts',
    'appid': api_key
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=params)
print(response.json()['hourly'])
