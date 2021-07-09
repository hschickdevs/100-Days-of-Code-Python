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
            self.add_segment(pos)

    def add_segment(self, position):
        self.segments.append(Turtle('square'))
        self.segments[-1].color('white')
        self.segments[-1].pu()
        self.segments[-1].goto(position)

    def extend(self):
        self.add_segment(self.segments[-1].pos())

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

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
