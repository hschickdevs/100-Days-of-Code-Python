from turtle import Screen
from quiz_handler import QuizHandler
import time as t

screen = Screen()
screen.title("U.S. States Guessing Game")
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")

handler = QuizHandler()

TIMER_WAIT = 0
BOT = False

game_is_on = True
while game_is_on:
    if handler.game_is_over():
        report = screen.textinput("YES or NO", "Generate Learning Report?").lower()
        if report == "yes":
            handler.generate_report()
            handler.end_game()
        else:
            handler.end_game()
        game_is_on = False
    else:
        handler.new_state()
        if BOT:
            answer = handler.state_name.lower()
        else:
            answer = screen.textinput("Guess the State!", f"({handler.question_number}/50) Type your answer: ").lower()
        if answer == handler.state_name.lower():
            handler.check_answer(True)
        else:
            handler.check_answer(False)
        t.sleep(TIMER_WAIT)


handler.new_state()

screen.exitonclick()