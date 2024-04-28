from tkinter import *

window = Tk()
window.title("Password Generator")
window.config(pady=50, padx=50, bg='yellow')


# Logo
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, padx=3, pady=3, columnspan=2)


# Label

website_label = Label(text='Website :')
website_label.grid(column=0, row=1, pady=3, padx=3)
email_label = Label(text='Email/Username :')
email_label.grid(column=0, row=2, pady=3, padx=3)
password_label = Label(text='Password :')
password_label.grid(column=0, row=3, pady=3, padx=3)


# Entry Field

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, pady=3, padx=3)
email_entry = Entry(width=21)
email_entry.grid(row=2, column=1, pady=3, padx=3)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=3, padx=3)


# Buttons

password_button = Button(text="Generate password", width=15)
password_button.grid(column=2, row=3, columnspan=2)
search_button = Button(text="Search", width=15)
search_button.grid(column=2, row=1, columnspan=2)
add_button = Button(text="ADD", width=35)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()