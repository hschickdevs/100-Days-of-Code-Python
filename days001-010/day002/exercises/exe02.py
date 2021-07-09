# 🚨 Don't change the code below 👇
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
weight = float(weight)

bmi = int(weight / height ** 2)
print(bmi)
