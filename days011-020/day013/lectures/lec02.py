from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]

# Reproduce the Bug
# The problem is that dice_num is in the interval [1, 6]
# and the indexes of dice_imgs are in the interval [0, 5]
# Therefore, currently 0 is never picked and sometimes 6,
# is chosen which gives an IndexError.
# dice_num = randint(1, 6)

# IndexError
# print(dice_imgs[6])

dice_num = randint(0, 5)
print(dice_imgs[dice_num])
