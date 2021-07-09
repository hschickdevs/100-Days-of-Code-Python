programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

print(programming_dictionary["Bug"])

# KeyError
# print(programming_dictionary["Bog"])

random_dict = {
    123: 'Chocolate'
}

print(random_dict[123])

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary)

programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

empty_dict = {}

print(empty_dict)

programming_dictionary = {}
print(programming_dictionary)

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)
print()

for key in programming_dictionary:
    print(f"{key} -> {programming_dictionary[key]}")

