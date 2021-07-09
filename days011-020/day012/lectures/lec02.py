def create_enemy():
    enemies1 = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy1 = enemies1[0]
    print(new_enemy1)


game_level = 3
enemies2 = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy2 = enemies2[0]
print(new_enemy2)

create_enemy()

# NameError
# print(new_enemy1)
