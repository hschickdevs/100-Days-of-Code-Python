import os
import requests


def bring_umbrella(data):
    for hour_data in data[:12]:
        if hour_data['weather'][0]['id'] < 700:
            return True
    return False


LATITUDE = 23.810651
LONGITUDE = 90.4126466

api_key = os.getenv('OWM_KEY')

params = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'exclude': 'current,minutely,daily,alerts',
    'appid': api_key
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=params)
response.raise_for_status()
weather_data = response.json()['hourly']
if bring_umbrella(weather_data):
    print("Bring an umbrella.")
else:
    print("No umbrella needed.")
