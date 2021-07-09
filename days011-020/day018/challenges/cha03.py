from random import shuffle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

colors = ['chartreuse', 'blue', 'dark green', 'dark orange', 'purple', 'salmon', 'red', 'crimson']
shuffle(colors)

tim.pu()
tim.goto(0, 100)
tim.pd()

for num_sides, color in enumerate(colors, 3):
    angle = 360 / num_sides
    tim.color(color)
    for _ in range(num_sides):
        tim.fd(100)
        tim.rt(angle)

screen.exitonclick()
