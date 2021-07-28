import os
import requests


# https://tequila.kiwi.com/portal/docs/tequila_api/search_api

# This class is responsible for grabbing and formatting the data
class FlightSearch:
    def __init__(self):
        self.header = {
            "apikey": os.environ.get("KIWI_API_KEY")
        }
        print(f'Kiwi Authorization: {self.header["apikey"]}')

    def get_direct_deals(self, tk_data):
        airports = tk_data['airport_codes']
        if not airports:
            fly_from_codes = self.to_IATA(tk_data['flights_information']['departure_cities'])
            fly_to_codes = self.to_IATA(tk_data['flights_information']['arrival_cities'])
        else:
            fly_from_codes = tk_data['flights_information']['departure_cities']
            fly_to_codes = tk_data['flights_information']['arrival_cities']

        layovers_bool = tk_data['layovers']

        endpoint = "https://tequila-api.kiwi.com/v2/search"
        query = {
            "fly_from": fly_from_codes,
            "fly_to": fly_to_codes,
            "date_from": tk_data['flights_information']['from_dates'],
            "date_to": tk_data['flights_information']['to_dates'],
            "curr": "USD",
            "price_from": 0,
            "adults": 1,
            # "price_to": max_price,
            "sort": "price",
            # "nights_in_dst_from": 7, <
            # "nights_in_dst_to": 28,  < These allow for round trips...
            # "flight_type": "round",  < (round or oneway)
        }

        if not layovers_bool:
            query["max_stopovers"] = 0

        if tk_data['trip_type'] == "round":
            query['flight_type'] = "round"
            query['nights_in_dst_from'] = tk_data['nights_in_destination']
            query['nights_in_dst_to'] = tk_data['nights_in_destination']

        tequila_response = requests.get(url=endpoint, params=query, headers=self.header)
        # print(tequila_response.json())
        tequila_response.raise_for_status()
        tequila_data = tequila_response.json()
        flight_deals = tequila_data['data']

        # GET CHEAPEST FLIGHT:
        cheapest_flight = 9999999
        cheapest_flight_index = 0
        for (index, data) in enumerate(flight_deals):
            if data['price'] < cheapest_flight and data['availability']['seats'] >= 1:
                cheapest_flight = data['price']
                cheapest_flight_index = index
        try:
            return flight_deals[cheapest_flight_index]
        except IndexError:
            return None

    def to_IATA(self, city):
        endpoint = "https://tequila-api.kiwi.com/locations/query"
        query = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
        }
        response = requests.get(url=endpoint, params=query, headers=self.header)
        response.raise_for_status()
        IATA_data = response.json()
        # return ','.join([location['id'] for location in IATA_data['locations']])
        try:
            return [location['id'] for location in IATA_data['locations']][0]
        except IndexError:
            return ""
