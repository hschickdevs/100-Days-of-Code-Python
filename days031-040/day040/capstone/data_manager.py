import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, url, headers, sheet):
        self.sheet_data = self.get(url, headers=headers)[sheet]

    @staticmethod
    def get(url, headers):
        return requests.get(url, headers=headers).json()

    def put(self, url, iata_codes, headers):
        for row_num, iata_code in iata_codes.items():
            data = {
                'price': {
                    'iataCode': iata_code
                }
            }
            headers['Content-Type'] = 'application/json'
            requests.put(f'{url}/{row_num}', json=data, headers=headers)
        del headers['Content-Type']
        self.sheet_data = self.get(url, headers=headers)


if __name__ == '__main__':
    import os

    sheet_url = 'https://api.sheety.co/050bd07b012d60f91d54ee8c95675f8c/flightDeals/prices'
    sheet_headers = {'Authorization': f"Bearer {os.getenv('SHEETY_TOKEN')}"}
    data_manager = DataManager(sheet_url, sheet_headers)
    sheet_data = data_manager.sheet_data
    print(sheet_data)
    data_manager.put(sheet_url, {2: '', 3: '', 4: ''}, sheet_headers)
    sheet_data = data_manager.sheet_data
    print(sheet_data)
