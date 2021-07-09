import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))
print()

year = now.year
month = now.month
weekday = now.weekday()
print(f'year: {year}, month: {month}, weekday: {weekday}')

birthday = dt.datetime(year=1996, month=6, day=21, hour=7, minute=20)
print(birthday)
