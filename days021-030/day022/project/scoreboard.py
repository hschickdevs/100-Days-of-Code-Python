from turtle import Turtle

FONT = ('Atari Classic Chunky', 45, 'normal')
WINNER_FONT = ('Atari Classic Chunky', 20, 'normal')
MAX_SCORE = 7


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.pu()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 200)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f'{self.left_score}   {self.right_score}', align='center', font=FONT)

    def is_game_over(self):
        return self.left_score == MAX_SCORE or self.right_score == MAX_SCORE

    def point(self, side):
        if side == 'l':
            self.left_score += 1
        else:
            self.right_score += 1
        self.write_score()

    def get_winner(self):
        if self.left_score == MAX_SCORE:
            return 'Left Player'
        else:
            return 'Right Player'

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
        self.goto(0, -100)
        self.write(f"The winner is:\n {self.get_winner()}", align='center', font=WINNER_FONT)
