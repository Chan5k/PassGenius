import string
import random
import tkinter as tk
from tkinter import messagebox

# Define the main window
window = tk.Tk()
window.title("PassGenius")
window.geometry("400x350")

# Define the password variable
password = tk.StringVar()
password_label = tk.Label(window, textvariable=password)

# Define the password strength variable
password_strength = tk.StringVar()
password_strength_label = tk.Label(window, textvariable=password_strength)

# Define the password length scale
length_label = tk.Label(window, text="Password Length")
length_label.pack()
length_scale = tk.Scale(window, from_=8, to=32, orient="horizontal")
length_scale.pack()

# Define the password character options
options_frame = tk.Frame(window)
options_frame.pack()

use_uppercase = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(options_frame, text="Uppercase", variable=use_uppercase)
uppercase_checkbox.pack(side=tk.LEFT)

use_lowercase = tk.BooleanVar()
lowercase_checkbox = tk.Checkbutton(options_frame, text="Lowercase", variable=use_lowercase)
lowercase_checkbox.pack(side=tk.LEFT)

use_digits = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(options_frame, text="Digits", variable=use_digits)
digits_checkbox.pack(side=tk.LEFT)

use_special = tk.BooleanVar()
special_checkbox = tk.Checkbutton(options_frame, text="Special Characters", variable=use_special)
special_checkbox.pack(side=tk.LEFT)

# Define the generate password function
def generate_password():
    # Get the password length
    length = length_scale.get()

    # Define the character set to use
    character_set = ""
    if use_uppercase.get():
        character_set += string.ascii_uppercase
    if use_lowercase.get():
        character_set += string.ascii_lowercase
    if use_digits.get():
        character_set += string.digits
    if use_special.get():
        character_set += string.punctuation

    # Check if at least one option is selected
    if not character_set:
        messagebox.showerror("Error", "Please select at least one option")
        return

    # Generate the password
    password_value = "".join(random.choices(character_set, k=length))
    password.set(password_value)

    # Determine the password strength
    strength = 0
    if use_uppercase.get():
        strength += 1
    if use_lowercase.get():
        strength += 1
    if use_digits.get():
        strength += 1
    if use_special.get():
        strength += 1
    if length >= 12:
        strength += 1

    # Set the password strength label based on the strength
    if strength <= 2:
        password_strength.set("Weak")
        password_strength_label.config(fg="red")
    elif strength == 3:
        password_strength.set("Medium")
        password_strength_label.config(fg="orange")
    else:
        password_strength.set("Strong")
        password_strength_label.config(fg="green")

# Define the generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Define the copy password function
def copy_password():
    window.clipboard_clear()
    window.clipboard_append(password.get())

# Define the copy password button
copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack(pady=10)

# Show the password label
password_label.pack(pady=10)

# Show the password strength label
password_strength_label.pack(pady=5)

# Start the main loop
window.mainloop()