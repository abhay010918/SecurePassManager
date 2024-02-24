from tkinter import *
from tkinter import messagebox

# Password Generator Project
from random import *

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)
    entry_pass.delete(0, END)
    entry_pass.insert(0, password)

# Save Password
def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_pass.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Invalid input", message="Please fill in all fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_web.delete(0, END)
                entry_pass.delete(0, END)
                entry_email.delete(0, END)

# Create the main window
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="#87CEEB")  # Set a sky blue background

# Load the image
logo = PhotoImage(file='logo1.png')

# Create a canvas and add the image to it
canvas = Canvas(window, width=300, height=300, bg="#87CEEB")
canvas.create_image(150, 150, anchor=CENTER, image=logo)
canvas.grid(row=0, column=1)

# Creating all the labels
web_label = Label(window, text="Website", bg="#87CEEB", font=("Arial", 12, "bold"))  # Set label background color and font
web_label.grid(row=1, column=0, pady=(10, 0))
email_label = Label(window, text="Email/Username", bg="#87CEEB", font=("Arial", 12, "bold"))  # Set label background color and font
email_label.grid(row=2, column=0)
pass_label = Label(window, text="Password", bg="#87CEEB", font=("Arial", 12, "bold"))  # Set label background color and font
pass_label.grid(row=3, column=0)

# Creating entry widgets
entry_web = Entry(window, width=30, font=("Arial", 12))
entry_web.grid(row=1, column=1, padx=10, pady=(10, 0))
entry_web.focus()
entry_email = Entry(window, width=30, font=("Arial", 12))
entry_email.grid(row=2, column=1, padx=10)
entry_email.insert(0, "example@gmail.com")
entry_pass = Entry(window, width=30, font=("Arial", 12))
entry_pass.grid(row=3, column=1, padx=10)

# Creating buttons
gen_pass = Button(window, text="Generate Password", command=password_generator, bg="#1E90FF", fg="white", font=("Arial", 12, "bold"))  # Set button background and text color
gen_pass.grid(row=4, column=1, padx=10, pady=(10, 0))
add_pass = Button(window, text="Add", command=save, bg="#32CD32", fg="white", font=("Arial", 12, "bold"))  # Set button background and text color
add_pass.grid(row=5, column=1, pady=10)

# Start the Tkinter event loop
window.mainloop()
