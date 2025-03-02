import random
import requests
import string
import tkinter as tk
from tkinter import messagebox

def get_random_name():
    url = "https://randomuser.me/api/?inc=name&nat=us"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        first_name = data['results'][0]['name']['first']
        last_name = data['results'][0]['name']['last']
        return f"{first_name} {last_name}"
    else:
        return "Error fetching name"

def generate_email(name):
    if "Error" not in name:
        nickname = name.replace(" ", ".").lower()
        number = random.randint(1, 100)
        return f"{nickname}{number}@example.com"
    else:
        return "Error generating email"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_name_and_email():
    full_name = get_random_name()
    email = generate_email(full_name)
    name_label.config(text=f"Generated Name: {full_name}")
    email_label.config(text=f"Generated Email: {email}")

def generate_new_password():
    length = password_length_scale.get()
    password = generate_password(length)
    password_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Random Name, Email, and Password Generator")

# Create and place the labels and buttons
name_label = tk.Label(root, text="Generated Name: ")
name_label.pack()

email_label = tk.Label(root, text="Generated Email: ")
email_label.pack()

password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

generate_name_email_button = tk.Button(root, text="Generate Name and Email", command=generate_name_and_email)
generate_name_email_button.pack()

generate_password_button = tk.Button(root, text="Generate Password", command=generate_new_password)
generate_password_button.pack()

# Create and place the scale for password length
password_length_scale = tk.Scale(root, from_=8, to_=128, orient=tk.HORIZONTAL, label="Password Length")
password_length_scale.set(12)  # Default length
password_length_scale.pack()

# Run the application
root.mainloop()