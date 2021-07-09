age: int
name: str
height: float
is_human: bool


def police_check(a_age: int) -> bool:
    return a_age >= 18


age = 24
name = "Paula"
height = 1.62
is_human = True
print(age, name, height, is_human)

age = int(input("Your age: "))
if police_check(age):
    print("You may pass")
else:
    print("Pay a fine")


