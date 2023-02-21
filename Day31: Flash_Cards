from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
random_card = None

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    word_dict = df.to_dict(orient="records")
else:
    word_dict = df.to_dict(orient="records")


def word_learned():
    global random_card
    word_dict.remove(random_card)
    next_card()


def next_card():
    global random_card, flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(word_dict)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global random_card
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, func=flip_card)

# images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 269, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_button = Button(image=right_img, highlightthickness=0, command=word_learned)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

language_text = canvas.create_text(400, 150, text="Language", fill="black", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))

next_card()

window.mainloop()

final_df = pandas.DataFrame(word_dict)
final_df.to_csv("data/words_to_learn.csv", index=False)
