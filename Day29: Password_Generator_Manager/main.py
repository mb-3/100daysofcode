from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import pandas as pd


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for letter in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    pw_input = pw_entry.get()

    if len(website_input) == 0 or len(pw_input) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input,
                                       message=f"These are the details entered: \nEmail: {email_input} "
                                               f"\nPassword: {pw_input} \nIs it okay to save?-")
        if is_ok:
            entry = {
                'Website': [website_input],
                'Email': [email_input],
                'Not': [pw_input]
            }
            entry_df = pd.DataFrame(entry)
            entry_df.to_csv("C:\\Users\AyoooPC\Desktop\\not_it.csv", mode='a', index=False, header=False)
            website_entry.delete(0, END)
            pw_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# LABELS
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# ENTRIES
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(END, "mattb13777@gmail.com")
pw_entry = Entry(width=21)
pw_entry.grid(column=1, row=3, sticky="EW")

# BUTTONS
pw_button = Button(text="Generate Password", command=generate_pw)
pw_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
