from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__('turtle')
        self.penup()
        self.seth(90)
        self.set_player()

    def set_player(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        return self.ycor() >= 280

    def move(self):
        self.fd(MOVE_DISTANCE)

    def game_over(self):
        self.ht()
