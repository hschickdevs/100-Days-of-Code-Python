from turtle import Turtle, Screen


def move_forwards():
    tim.forward(10)


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key='space', fun=move_forwards)

screen.exitonclick()

