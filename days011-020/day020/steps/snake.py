from turtle import Turtle

STARTING_POS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.segments.append(Turtle('square'))
            self.segments[-1].color('white')
            self.segments[-1].pu()
            self.segments[-1].goto(pos)

    def move(self):
        for idx in range(len(self.segments) - 1, 0, -1):
            pos = self.segments[idx - 1].pos()
            self.segments[idx].goto(pos)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
