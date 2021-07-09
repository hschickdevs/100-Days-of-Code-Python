with open('file1.txt') as file:
    numbers1 = [int(line) for line in file.readlines()]

with open('file2.txt') as file:
    numbers2 = [int(line) for line in file.readlines()]

result = [n for n in numbers1 if n in numbers2]

# Write your code above 👆

print(result)
