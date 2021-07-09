import os
import requests

from twilio.rest import Client


def bring_umbrella(data):
    for hour_data in data[:12]:
        if hour_data['weather'][0]['id'] < 700:
            return True
    return False


LATITUDE = 23.810651
LONGITUDE = 90.4126466

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
phone_number = os.environ['TWILIO_NUMBER']
my_number = os.environ['MY_NUMBER']
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
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="☔️ It's going to rain today.\n Remember to bring an umbrella ☂️",
        from_=phone_number,
        to=my_number)
    print(message.status)
