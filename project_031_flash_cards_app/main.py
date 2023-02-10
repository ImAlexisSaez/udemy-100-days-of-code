import pandas
import random
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
LANGUAGE_POS = (400, 150)
LANGUAGE_WORD_FONT = ("Ariel", 60, "bold")
LANGUAGE_WORD_POS = (400, 263)


# Generate a word
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_image, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.csv("data/words_to_learn.csv", index=False)
    next_card()


# Read data
current_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Window
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tk.PhotoImage(file="images/card_front.png")
card_back_image = tk.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(LANGUAGE_POS, text="", font=LANGUAGE_FONT)
card_word = canvas.create_text(LANGUAGE_WORD_POS, text="", font=LANGUAGE_WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
fail_image = tk.PhotoImage(file="images/wrong.png")
fail_button = tk.Button(image=fail_image, highlightthickness=0, borderwidth=0, command=next_card)
fail_button.grid(row=1, column=0)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image, highlightthickness=0, borderwidth=0, command=is_known)
right_button.grid(row=1, column=1)

# Generates the first card:
next_card()

window.mainloop()
