from tkinter import *
from tkinter import messagebox
from letters_numbers_symbols import letters, numbers, symbols
from random import choice, shuffle, randint
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = [choice(letters) for letter in range(randint(8, 10))]
    password += [choice(numbers) for number in range(randint(2, 4))]
    password += [choice(symbols) for symbol in range(randint(2, 4))]
    shuffle(password)
    pw = "".join(password)
    pyperclip.copy(pw)
    password_entry.delete(0, END)
    password_entry.insert(END, pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as data_file:
        website = website_entry.get()
        email = email_username_entry.get()
        password = password_entry.get()

        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        else:
            is_ok = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered: \nEmail: {email} \n"
                                                   f"Password: {password}\nDo you want to save data?")

            if is_ok:
                data_file.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0, END)
                # email_username_entry.delete(0, END)
                password_entry.delete(0, END)
            elif not is_ok:
                messagebox.showwarning(title="Canceled", message="Data will not be saved!")
                website_entry.delete(0, END)
                # email_username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# Texts
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
email_username_text = Label(text="Email/Username:")
email_username_text.grid(row=2, column=0)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

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
email_username_entry.grid(row=2, column=1)
email_username_entry.insert(END, "Nikagagua@live.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Buttons
generate_button = Button(text="Generate Password", width=30, borderwidth=1, command=generate_password)
generate_button.grid(row=4, column=1)

add_button = Button(text="Add", width=30, borderwidth=1, command=save)
add_button.grid(row=5, column=1)

window.mainloop()
