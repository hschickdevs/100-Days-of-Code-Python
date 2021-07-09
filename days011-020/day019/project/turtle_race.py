from random import shuffle, randint
from turtle import Turtle, Screen


def create_turtles():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

    turtles = []
    for color in colors:
        turtles.append(Turtle('turtle'))
        turtles[-1].color(color)
        turtles[-1].pu()

    y = -90
    for turtle in turtles:
        turtle.goto(-230, y)
        y += 30

    return turtles


def move(turtles):
    shuffle(turtles)
    for turtle in turtles:
        turtle.fd(randint(0, 10))
        if turtle.xcor() >= 230:
            return turtle.pencolor()
    return move(turtles)


def race():
    turtles = create_turtles()
    bet = screen.textinput(
        title='Make your bet!', prompt='Which turtle will win the race? Enter a rainbow color: ').lower()
    winning_color = move(turtles)

    print(f"The {winning_color} turtle won the race!")
    if winning_color == bet:
        print("You won!")
    else:
        print("You lost!")


screen = Screen()
screen.setup(width=500, height=400)

race()

screen.exitonclick()
