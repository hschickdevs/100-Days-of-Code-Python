import requests


class FlightSearch:
    def __init__(self, url, params, headers):
        self.flight_data = self.get(url, params, headers)

    @staticmethod
    def get(url, params, headers):
        return requests.get(f'{url}locations/query', params=params, headers=headers).json()['locations'][0]


if __name__ == '__main__':
    import os

    tequila_params = {
        'location_types': 'city',
        'term': 'london'
    }
    tequila_headers = {'apikey': os.getenv('TEQUILA_KEY')}

    flight_search = FlightSearch('https://tequila-api.kiwi.com/', tequila_params, tequila_headers)
    print(flight_search.flight_data)

