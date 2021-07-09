import pandas as pd


def to_fahrenheit(temp):
    return round(temp * 1.8 + 32, 2)


data = pd.read_csv('weather_data.csv')
print(type(data))
print(type(data['temp']))

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

print(data['temp'].mean())
print(data['temp'].max())
print()

print(data['condition'])
print(data.condition)
print()

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print()

print(to_fahrenheit(int(monday.temp)))
print()

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pd.DataFrame(data_dict)
print(data)
data.to_csv("students_data.csv", index=False)
