weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


# 🚨 Don't change code above 👆

# Write your code below 👇
def to_fahrenheit(temp):
    return round(temp * 1.8 + 32, 1)


weather_f = {weekday: to_fahrenheit(temp) for weekday, temp in weather_c.items()}
print(weather_f)
