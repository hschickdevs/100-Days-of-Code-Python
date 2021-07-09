from random import choice
from turtle import Turtle, Screen, colormode


def random_color():
    colors = [(10, 9, 3), (95, 99, 79), (0, 255, 0), (82, 255, 184),
              (251, 177, 60), (255, 233, 0), (68, 3, 129), (216, 17, 89)]
    return choice(colors)


def draw_line(num_dots):
    for _ in range(num_dots):
        tim.dot(20, random_color())
        tim.fd(50)


colormode(255)
tim = Turtle(visible=False)
screen = Screen()

tim.pu()
tim.speed(0)

tim.goto(-250, 250)
for y in range(-250, 250, 50):
    tim.goto(-250, y)
    draw_line(10)

screen.exitonclick()
