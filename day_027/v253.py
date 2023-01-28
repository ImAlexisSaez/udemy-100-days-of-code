import tkinter


def button_clicked():
    my_label.config(text=input_text.get())


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=200, pady=200)  # Padding

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = tkinter.Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New button!")
new_button.grid(column=2, row=0)

# Entry
input_text = tkinter.Entry(width=10)
input_text.grid(column=3, row=2)


window.mainloop()
