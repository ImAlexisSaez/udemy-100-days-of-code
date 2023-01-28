import tkinter


def miles_to_km():
    miles = float(input_text.get())
    km = 1.609344 * miles
    result_label.config(text=f"{km:.2f}")


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=150, height=150)
window.config(padx=50, pady=50)

# Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0")
result_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)

# Button
button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

# Entry
default_miles = tkinter.StringVar(value="0")
input_text = tkinter.Entry(width=10, textvariable=default_miles)
input_text.focus()
input_text.grid(row=0, column=1)


window.mainloop()
