import random

import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

random_float = random.random()
print(random_float)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')
