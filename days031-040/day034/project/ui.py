from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
RED = "#FF3333"
GREEN = "#99FF33"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='Question HERE', width=280,
                                                     font=('Crafty Girls', 16, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_img = PhotoImage(file='images/true.png')
        wrong_img = PhotoImage(file='images/false.png')

        self.right_button = Button(image=right_img, highlightthickness=0, command=self.press_right)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.press_wrong)
        self.wrong_button.grid(column=1, row=2)

        self.score = Label(text=f'Score: {self.quiz.score}',
                           font=('Crafty Girls', 12, 'bold'),
                           bg=THEME_COLOR, fg='white')
        self.score.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.score.config(text=f'Final score: {self.quiz.score}')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def press_right(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def press_wrong(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)
        self.window.after(1000, self.get_next_question)

