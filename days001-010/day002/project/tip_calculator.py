print("🧮 Welcome to the Tip Calculator! 🧮")

bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100
num_people = int(input("How many people to split the bill? "))

final_bill = bill * (1 + percentage_tip)
bill_per_person = final_bill / num_people
print(f"🧮 Each person should pay: ${bill_per_person:.2f} 🧮")
