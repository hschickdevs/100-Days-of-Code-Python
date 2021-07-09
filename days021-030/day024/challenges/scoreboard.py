from turtle import Turtle

ALIGNMENT = 'center'
FONT_SCORE = ('Atari Classic Chunky', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.score = 0
        self.high_score = None
        self.set_high_score()
        self.pu()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def set_high_score(self):
        with open('data.txt') as file:
            self.high_score = int(file.read())

    def save_high_score(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', font=FONT_SCORE, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

