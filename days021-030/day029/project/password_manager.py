# ------------------------------------------------------ IMPORTS ----------------------------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint

from pyperclip import copy

# ---------------------------------------------------- CONSTANTS ----------------------------------------------------- #
FONT = ("Atari Classic Extrasmooth", 8)
LETTERS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
SYMBOLS = ('!', '#', '$', '%', '&', '(', ')', '*', '+')


# ------------------------------------------------- PASSWORD GENERATOR ----------------------------------------------- #
def gen_password():
    password_entry.delete(0, END)
    letters = [choice(LETTERS) for _ in range(randint(8, 10))]
    numbers = [choice(NUMBERS) for _ in range(randint(2, 4))]
    symbols = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    password = letters + numbers + symbols
    shuffle(password)
    final_password = ''.join(password)
    copy(final_password)
    password_entry.insert(0, final_password)


# --------------------------------------------------- SAVE PASSWORD -------------------------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    if len(website) != 0 and len(user) and len(password) != 0:
        log = ' | '.join((website, user, password))
        message = f'This are the details entered:\nEmail/Username: {user}\nPassword: {password}\nIs it ok to save? '
        is_ok = messagebox.askokcancel(title=website, message=message)
        if is_ok:
            with open('data.txt', 'a') as file:
                print(log, file=file)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(title="🚨 Empty field 🚨", message="You left some field(s) empty. Please try again!")


# ------------------------------------------------------ UI SETUP ---------------------------------------------------- #
window = Tk()
window.title("🔐 Password Manager 🔐")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_title = Label(text='Website:', font=FONT)
website_title.grid(column=0, row=1)

user_title = Label(text='Email/Username:', font=FONT)
user_title.grid(column=0, row=2)

password_title = Label(text='Password:', font=FONT)
password_title.grid(column=0, row=3)

website_entry = Entry(width=40, font=FONT)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

user_entry = Entry(width=40, font=FONT)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(END, "paula@email.com")

password_entry = Entry(width=20, font=FONT)
password_entry.grid(column=1, row=3)

gen_button = Button(text="Generate Password", font=FONT, command=gen_password)
gen_button.grid(column=2, row=3)

save_button = Button(width=38, text="Add", font=FONT, command=save)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
