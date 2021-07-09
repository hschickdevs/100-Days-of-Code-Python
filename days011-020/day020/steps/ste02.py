import time
from turtle import Turtle, Screen

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("🐍 My Snake Game 🐍")
screen.tracer(0)

segments = []
for pos in STARTING_POS:
    segments.append(Turtle('square'))
    segments[-1].color('white')
    segments[-1].pu()
    segments[-1].goto(pos)

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    for idx in range(len(segments) - 1, 0, -1):
        pos = segments[idx - 1].pos()
        segments[idx].goto(pos)
    segments[0].fd(20)



screen.exitonclick()

