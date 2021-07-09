from turtle import Turtle, Screen


def move_forwards():
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def turn_left():
    tim.lt(10)


def turn_right():
    tim.rt(10)


def clear():
    tim.reset()


tim = Turtle()
screen = Screen()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
