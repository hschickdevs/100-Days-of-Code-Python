def increase_enemies1():
    # UnboundLocalError
    # enemies += 1
    pass


def increase_enemies2():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


def increase_enemies3():
    return enemies + 1


enemies = 1
increase_enemies2()
print(f"enemies outside function: {enemies}")

enemies = 1
print(f"enemies before function: {enemies}")
enemies = increase_enemies3()
print(f"enemies after function: {enemies}")
