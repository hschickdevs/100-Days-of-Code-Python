from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

for _ in range(4):
    tim.lt(90)
    tim.fd(100)

screen.exitonclick()
