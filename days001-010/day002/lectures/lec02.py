# TypeError
# print(len(4837))

num_char = len(input("What is your name? "))

# TypeError
# print("Your name has " + num_char + " characters.")

print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print()

a = 123
print(type(a))

a = str(123)
print(type(a))

a = float(123)
print(type(a))
print()

print(70 + float("100.5"))
print(str(70) + str(100))
