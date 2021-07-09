from turtle import Turtle

ALIGNMENT = 'center'
FONT_SCORE = ('Atari Classic Chunky', 20, 'normal')
FONT_GAME_OVER = ('Atari Classic Chunky', 36, 'normal')
FONT_GAME_OVER_SCORE = ('Atari Classic Chunky', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0

        self.pu()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Score: {self.score}', font=FONT_SCORE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', font=FONT_GAME_OVER, align=ALIGNMENT)
        self.goto(0, -100)
        self.write(f'Final score: {self.score}', font=FONT_GAME_OVER_SCORE, align=ALIGNMENT)
