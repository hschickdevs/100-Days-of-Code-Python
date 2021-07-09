from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("🐍 My Snake Game 🐍")

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []
for pos in starting_pos:
    segments.append(Turtle('square'))
    segments[-1].color('white')
    segments[-1].pu()
    segments[-1].goto(pos)

screen.exitonclick()

