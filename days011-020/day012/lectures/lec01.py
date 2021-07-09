def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


def drink_potion1():
    potion_strength = 2
    print(potion_strength)


def drink_potion2():
    print(player_health)


def game():
    def drink_potion3():
        print("Drinking...")

    drink_potion3()


enemies = 1
increase_enemies()
print(f"enemies outside function: {enemies}")

drink_potion1()

# NameError
# print(potion_strength)

player_health = 10
drink_potion2()
print(player_health)

game()

# NameError
# drink_potion3()
