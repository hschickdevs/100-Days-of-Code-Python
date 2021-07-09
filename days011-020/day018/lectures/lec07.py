from random import choice, randint
from turtle import Turtle, Screen, colormode


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


colormode(255)
tim = Turtle(visible=False)
screen = Screen()

tim.pensize(15)
tim.speed(0)
for _ in range(200):
    tim.seth(choice([0, 90, 180, 270]))
    tim.color(random_color())
    tim.fd(30)
1
screen.exitonclick()
