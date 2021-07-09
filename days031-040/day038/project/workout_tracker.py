import os

from datetime import datetime

import requests

APP_ID = os.getenv('NUTRI_ID')
API_KEY = os.getenv('NUTRI_KEY')
SHEETY_URL = 'https://api.sheety.co/050bd07b012d60f91d54ee8c95675f8c/myWorkouts/workouts'
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
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
exercise_data = response.json()['exercises']
print(exercise_data)
now = datetime.now()

headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
for exercise in exercise_data:
    row = {
        'date': now.strftime('%d/%m/%Y'),
        'time': now.strftime('%X'),
        'exercise': exercise['name'].title(),
        'duration': exercise['duration_min'],
        'calories': exercise['nf_calories']
    }
    response = requests.post(SHEETY_URL, json={'workout': row}, headers=headers)
