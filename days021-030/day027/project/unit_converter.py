from tkinter import *

FONT = ("Make Wonderful Moments Script", 30)


def to_km(num_miles):
    return 1.60934 * num_miles


def display_km():
    num_miles = float(entry.get())
    km_label['text'] = f'{to_km(num_miles):.2f}'


window = Tk()

window.title("️⛽️ Mile to Km Converter ⛽️")
window.config(padx=20, pady=20)

miles_text = Label(text='Miles', font=FONT)
km_text = Label(text='km', font=FONT)
result_text = Label(text='is equal to', font=FONT)
km_label = Label(text='0', font=FONT)

button = Button(text='Calculate', font=FONT, command=display_km)

entry = Entry(width=7, font=FONT)
entry.insert(END, '0')

miles_text.grid(column=2, row=0)
km_text.grid(column=2, row=1)
result_text.grid(column=0, row=1)
km_label.grid(column=1, row=1)
button.grid(column=1, row=2)
entry.grid(column=1, row=0)

window.mainloop()
