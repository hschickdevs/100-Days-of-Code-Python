import requests

url = "https://opentdb.com/api.php"

params = {
    'amount': 10,
    'type': 'boolean',
    'category': 18
}

response = requests.get(url, params=params)
response.raise_for_status()
question_data = response.json()['results']
