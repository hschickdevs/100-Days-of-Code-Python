numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
letters = [letter for letter in name]
print(letters)  # ['A', 'n', 'g', 'e', 'l', 'a']

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) >= 5]
print(long_names)
