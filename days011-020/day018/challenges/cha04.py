from random import choice
from turtle import Turtle, Screen

tim = Turtle(visible=False)
screen = Screen()

colors = ['chartreuse', 'blue', 'dark green', 'dark orange', 'purple', 'salmon', 'red', 'crimson']

tim.pensize(15)
tim.speed(0)
for _ in range(200):
    tim.seth(choice([0, 90, 180, 270]))
    tim.color(choice(colors))
    tim.fd(30)
1
screen.exitonclick()
