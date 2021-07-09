import os

from datetime import datetime

import requests

USERNAME = 'PIXELA_USERNAME'
TOKEN = os.getenv('PIXELA_TOKEN')
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'
pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()
pixel_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': input("How many pages did you read today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers={"X-USER-TOKEN": TOKEN})
print(response.text)
