# Fix the Errors
# age is a str so we can't compare it with 18 which is an int,
# block of code for the if is not indented, and missing the f,
# of the f-string.
# age = input("How old are you? ")
# if age >= 18:
# print("You can drive at age {age}.")

age = int(input("How old are you? "))
if age >= 18:
    print(f"You can drive at age {age}.")
