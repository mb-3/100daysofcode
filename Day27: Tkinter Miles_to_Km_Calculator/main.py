from tkinter import *

FONT = ("Arial", 10, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


def button_clicked():
    miles_val = float(miles_input.get())
    km_val = round(miles_val * 1.609344, 2)
    km_value.config(text=f"{km_val}")


miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

isequalto_label = Label(text="is equal to", font=FONT)
isequalto_label.grid(column=0, row=1)

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

km_value = Label(text="", font=FONT)
km_value.grid(column=1, row=1)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()

