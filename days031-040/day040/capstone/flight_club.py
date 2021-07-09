import os
import datetime as dt

import requests

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
sheet_url = 'https://api.sheety.co/050bd07b012d60f91d54ee8c95675f8c/flightDeals/prices'
sheet_headers = {'Authorization': f"Bearer {os.getenv('SHEETY_TOKEN')}"}
data_manager = DataManager(sheet_url, sheet_headers, 'prices')

tequila_url = 'https://tequila-api.kiwi.com/'
tequila_headers = {'apikey': os.getenv('TEQUILA_KEY')}
tequila_params = {
    'location_types': 'city',
    'term': ''
}

iata_codes = {}
for entry in data_manager.sheet_data:
    if len(entry['iataCode']) != 0:
        continue
    tequila_params['term'] = entry['city']
    flight_data = FlightSearch(tequila_url, tequila_params, tequila_headers).flight_data
    iata_codes[entry['id']] = flight_data['code']

if len(iata_codes) != 0:
    data_manager.put(sheet_url, iata_codes, sheet_headers)

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
future = tomorrow + dt.timedelta(days=180)
kiwi_params = {
    'fly_from': 'LON',
    'date_from': tomorrow.strftime('%d/%m/%Y'),
    'date_to': future.strftime('%d/%m/%Y'),
    'nights_in_dst_from': 7,
    'nights_in_dst_to': 28,
    'curr': 'GBP',
    'price_to': 0,
    'limit': 1,
    'max_stopovers': 0
}
flights = []
for entry in data_manager.sheet_data:
    kiwi_params['fly_to'] = entry['iataCode']
    kiwi_params['price_to'] = entry['lowestPrice']
    flight_data = FlightData(tequila_url, kiwi_params, tequila_headers)
    if flight_data.flight_data is not None:
        flights.append(flight_data)

notification_manager = NotificationManager(flights)

url = 'https://api.sheety.co/050bd07b012d60f91d54ee8c95675f8c/flightDeals/users'
user_manager = DataManager(url, sheet_headers, 'users')
data_users = user_manager.sheet_data

emails = []
for data_user in data_users:
    emails.append(data_user['email'])

notification_manager.send_emails(emails)
