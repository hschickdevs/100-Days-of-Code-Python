from turtle import Turtle

FONT = ('Atari Classic Chunky', 12, 'normal')
GAME_OVER_FONT = ('Atari Classic Chunky', 36, 'normal')

POSITION = (-220, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.level = 0
        self.pu()
        self.goto(POSITION)
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def game_over(self):
        self.reset()
        self.write("GAME OVER", align='center', font=GAME_OVER_FONT)
        self.goto(0, -50)
        self.write(f"Final level: {self.level}", align='center', font=FONT)
