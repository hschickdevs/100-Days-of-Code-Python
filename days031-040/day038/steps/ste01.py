import os

import requests

APP_ID = os.getenv('NUTRI_ID')
API_KEY = os.getenv('NUTRI_KEY')

exercise = input("Tell me which exercise you did? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

body = {
    "query": exercise,
    "gender": "female",
    "weight_kg": 77.1,
    "height_cm": 162,
    "age": 24
}

response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise', json=body, headers=headers)
print(response.json())
