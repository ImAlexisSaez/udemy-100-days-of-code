import json
import pyperclip
import random
import tkinter as tk
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list.extend([random.choice(letters) for _ in range(nr_letters)])
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text: {
            "email": email_text,
            "password": password_text
        }
    }

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)  # Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)  # Updating old data
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ------------------------ FIND PASSWORD --------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)  # Reading old data
    except FileNotFoundError:
        messagebox.showerror(
            title="Error",
            message="No data file found!."
        )
    else:
        website_text = website_entry.get()
        if website_text in data.keys():
            email_text = data[website_text]["email"]
            password_text = data[website_text]["password"]
            messagebox.showinfo(
                title=website_text,
                message=f"Email: {email_text}\nPassword: {password_text}"
            )
        else:
            messagebox.showinfo(title="Oops", message=f"No details for {website_text} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Padlock image
canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
padlock_img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text="Website:", bg="white")
website_label.grid(row=1, column=0, sticky=tk.E)
email_label = tk.Label(text="Email / Username:", bg="white")
email_label.grid(row=2, column=0, sticky=tk.E)
password_label = tk.Label(text="Password:", bg="white")
password_label.grid(row=3, column=0, sticky=tk.E)

# Entries
website_entry = tk.Entry(width=33)
website_entry.grid(row=1, column=1, columnspan=1, sticky=tk.NSEW)
website_entry.focus()
email_entry = tk.Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2, sticky=tk.NSEW)
email_entry.insert(0, "alexis@gmail.com")
password_entry = tk.Entry(width=33)
password_entry.grid(row=3, column=1, sticky=tk.NSEW)

# Buttons
search_button = tk.Button(text="Search", bg="white", command=find_password)
search_button.grid(row=1, column=2, sticky=tk.NSEW)
gen_password_button = tk.Button(text="Generate Password", bg="white", command=gen_password)
gen_password_button.grid(row=3, column=2, sticky=tk.NSEW)
add_button = tk.Button(text="Add", width=44, bg="white", command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky=tk.NSEW)

window.mainloop()
