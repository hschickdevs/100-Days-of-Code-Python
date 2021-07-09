import csv

import pandas as pd

with open('weather_data.csv') as data_file:
    raw_data = data_file.readlines()
    print(raw_data)

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    print(data)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
        print(row)
    print(temperatures)

print()
data = pd.read_csv('weather_data.csv')
print(data)
print(data['temp'])
