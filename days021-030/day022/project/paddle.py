from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__('square')
        self.speed(0)
        self.pu()
        self.goto(pos)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        if y < 280:
            self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        if y > -280:
            self.goto(x, y)
