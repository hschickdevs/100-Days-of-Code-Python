def is_leap(a_year):
    return a_year % 4 == 0 and a_year % 100 != 0 or a_year % 400 == 0


def days_in_month(a_year, a_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a_month == 2 and is_leap(a_year):
        return 29
    return month_days[a_month - 1]


# 🚨 Do NOT change any of the code below 👇
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
