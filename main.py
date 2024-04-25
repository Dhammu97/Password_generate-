from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# logo
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=2)
# label

website_label = Label(text="Website :")
website_label.grid(row=1, column=0)
email_label = Label(text="Email :")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# entry

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons

add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1)
search_button = Button(text="Search", width=13)
search_button.grid(row=1, column=2)
pass_gen = Button(text="Generate Password")
pass_gen.grid(row=3, column=2)

window.mainloop()
