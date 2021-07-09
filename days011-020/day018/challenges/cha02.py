from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for _ in range(15):
    tim.fd(10)
    tim.pu()
    tim.fd(10)
    tim.pd()

screen.exitonclick()

