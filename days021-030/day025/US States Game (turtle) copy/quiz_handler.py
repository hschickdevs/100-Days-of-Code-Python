import random

import pandas
import pandas as pd
from turtle import Turtle

STATES_DATA = pd.read_csv("50_states.csv")
STATE_NAMES = STATES_DATA.state


class QuizHandler(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.question_number = 0
        self.setheading(90)
        self.state_name = ""
        self.used_states = []
        self.states_correct = []
        self.states_missed = []

    def new_state(self):
        self.color("black")
        new_state = random.choice(STATE_NAMES)
        if new_state in self.used_states:
            self.new_state()
        else:
            self.state_name = new_state
            self.used_states.append(self.state_name)
            self.question_number += 1
            state_location_row = STATES_DATA[STATES_DATA.state == self.state_name]
            self.goto(int(state_location_row.x), int(state_location_row.y))

    def game_is_over(self):
        if self.question_number < len(STATES_DATA):
            return False
        else:
            return True

    def end_game(self):
        self.color("black")
        self.hideturtle()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER. You scored {self.score}/{len(STATE_NAMES)}", move=False, align="center",
                   font=("Courier", 24, "normal"))

    def generate_report(self):
        missed_len = len(self.states_missed)
        correct_len = len(self.states_correct)
        if missed_len > correct_len:
            for num in range(missed_len - correct_len):
                self.states_correct.append("-")
        elif missed_len < correct_len:
            for num in range(correct_len - missed_len):
                self.states_missed.append("-")
        report_dict = {
            "States Missed": self.states_missed,
            "States Correct": self.states_correct
        }
        pandas.DataFrame(report_dict).to_csv("Learning-Report.csv")

    def check_answer(self, tf):
        if tf:
            self.color("green")
            self.score += 1
            self.states_correct.append(self.state_name)
        else:
            self.color("red")
            self.states_missed.append(self.state_name)
        self.write(arg=self.state_name, move=False, align="center", font=("Courier", 10, "normal"))
