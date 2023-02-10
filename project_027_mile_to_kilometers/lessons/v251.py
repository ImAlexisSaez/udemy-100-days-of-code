import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24))
my_label.pack(side="top")  # show the label
my_label.config(text="New text!")

# Button


def button_clicked():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click me!", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()


window.mainloop()
