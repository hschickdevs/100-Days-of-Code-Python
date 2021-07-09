import time

from datetime import datetime, timedelta

import requests


class FlightData:
    def __init__(self, url, params, headers):

        self.flight_data = self.get(url, params, headers)

        self.stop_overs = None
        self.via_city = None
        if self.flight_data is not None:
            self.fly_from = self.flight_data['flyFrom']
            self.city_from = self.flight_data['cityFrom']
            self.fly_to = self.flight_data['flyTo']
            self.city_to = self.flight_data['cityTo']
            self.price = self.flight_data['price']
            self.departure = time.strftime('%d-%m-%Y', time.localtime(self.flight_data['route'][0]['dTime']))
            self.arrival = time.strftime('%d-%m-%Y', time.localtime(self.flight_data['route'][1]['dTime']))

    def get(self, url, params, headers):
        response = requests.get(f'{url}search', params=params, headers=headers)
        try:
            data = response.json()['data'][0]
        except IndexError:
            params['max_stopovers'] = 1
            try:
                data = response.json()['data'][0]
            except IndexError:
                print(f"No flights found for {params['fly_from']}")
                return None
            else:
                print('Flight found!')
                self.stop_overs = 1
                self.via_city = self.flight_data['route'][0]['cityTo']
                return data
        else:
            print('Flight found')
            self.stop_overs = 0
            return data


if __name__ == '__main__':
    import os

    tomorrow = datetime.now() + timedelta(days=1)
    future = tomorrow + timedelta(days=180)
    kiwi_params = {
        'fly_from': 'LON',
        'fly_to': 'DPS',
        'date_from': tomorrow.strftime('%d/%m/%Y'),
        'date_to': future.strftime('%d/%m/%Y'),
        'nights_in_dst_from': 7,
        'nights_in_dst_to': 28,
        'curr': 'GBP',
        'price_to': 5700,
        'limit': 1,
        'max_stopovers': 0
    }
    kiwi_headers = {'apikey': os.getenv('TEQUILA_KEY')}
    flight = FlightData('https://tequila-api.kiwi.com/', kiwi_params, kiwi_headers)
    print(flight.flight_data)
