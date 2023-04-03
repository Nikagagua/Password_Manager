from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = [choice(letters) for _ in range(randint(8, 10))]
    password += [choice(numbers) for _ in range(randint(2, 4))]
    password += [choice(symbols) for _ in range(randint(2, 4))]
    shuffle(password)
    pw = "".join(password)
    pyperclip.copy(pw)
    password_entry.delete(0, END)
    password_entry.insert(END, pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    data = {}
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        new_data = {
            website: {
                "Email": email,
                "Password": password,
            }
        }

        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            pass

        data.update(new_data)
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email} \n"
                                               f"Password: {password}\nDo you want to save data?")
        if is_ok:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            messagebox.showwarning(title="Canceled", message="Data will not be saved!")
            website_entry.delete(0, END)
            # email_username_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="OOPS!", message="No Data File Found")
    else:
        website_data = {k: v for k, v in data.items() if k == website}
        if website_data:
            email_value = website_data[website]["Email"]
            password_value = website_data[website]["Password"]
            messagebox.showinfo(title=f"{website}",
                                message=f"Email: {email_value}\nPassword: {password_value}")
        else:
            messagebox.showwarning(title="Oops", message=f"No details for {website} exists.")
    finally:
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Texts
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
email_username_text = Label(text="Email/Username:")
email_username_text.grid(row=3, column=0)
password_text = Label(text="Password:")
password_text.grid(row=4, column=0)

# Image
canvas = Canvas(height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(row=3, column=1)
email_username_entry.insert(END, "Nikagagua@live.com")
password_entry = Entry(width=35)
password_entry.grid(row=4, column=1)

# Buttons
generate_button = Button(text="Generate Password", width=30, borderwidth=1, command=generate_password)
generate_button.grid(row=5, column=1)

add_button = Button(text="Add", width=30, borderwidth=1, command=save)
add_button.grid(row=6, column=1)

search_button = Button(text="Search", width=30, borderwidth=1, command=find_password)
search_button.grid(row=2, column=1)

window.mainloop()
