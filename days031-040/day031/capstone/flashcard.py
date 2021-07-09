# ----------------------------------------------------- IMPORTS ------------------------------------------------------ #
from tkinter import *
from random import choice
import pandas as pd

# ----------------------------------------------------- CONSTANTS ---------------------------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
END_COLOR = "#FFAE03"
FRENCH_COLOR = "#7F2CCB"
ENGLISH_COLOR = "#EF476F"
FONT_NAME = "Bonbon"


# ----------------------------------------------------- FUNCTIONS ---------------------------------------------------- #
def get_data():
    try:
        df = pd.read_csv('data/words_to_learn.csv')
    except FileNotFoundError:
        df = pd.read_csv('data/french_words.csv')
    finally:
        df_dict = df.to_dict(orient='records')
        return df_dict


def flip():
    title = 'English'
    canvas.itemconfig(card_image, image=back_img)
    canvas.itemconfig(title_text, text=title, fill=ENGLISH_COLOR)
    canvas.itemconfig(word_text, text=current_card[title], fill=ENGLISH_COLOR)


def right():
    data.remove(current_card)
    next_card()
    pd.DataFrame(data).to_csv('data/words_to_learn.csv', index=False)


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = choice(data)
    canvas.itemconfig(card_image, image=front_img)
    canvas.itemconfig(title_text, text='French', fill=FRENCH_COLOR)
    canvas.itemconfig(word_text, text=current_card['French'], fill=FRENCH_COLOR)
    timer = window.after(3000, flip)


# ------------------------------------------------- GLOBAL VARIABLES ------------------------------------------------- #
data = get_data()
current_card = {}

# ----------------------------------------------------- UI SETUP ----------------------------------------------------- #
window = Tk()
window.title("📝 Flashy 📝️")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip)

back_img = PhotoImage(file='images/card_back.png')
front_img = PhotoImage(file='images/card_front.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=front_img)

title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, highlightthickness=0, command=right)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
