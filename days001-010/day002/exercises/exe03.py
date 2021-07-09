# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years_left = 90 - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
