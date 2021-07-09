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

tim.speed(0)
for heading in range(0, 360, 5):
    tim.seth(heading)
    tim.color(random_color())
    tim.circle(100)

screen.exitonclick()
