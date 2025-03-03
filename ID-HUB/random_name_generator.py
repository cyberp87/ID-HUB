import random
import requests
import string
import tkinter as tk
from tkinter import messagebox
import config

def get_random_name(nationality):
    url = f"https://randomuser.me/api/?inc=name&nat={nationality}"
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
    nationality = nationality_var.get()
    full_name = get_random_name(nationality)
    email = generate_email(full_name)
    name_label.config(text=f"Generated Name: {full_name}")
    email_label.config(text=f"Generated Email: {email}")

def generate_new_password():
    length = password_length_scale.get()
    password = generate_password(length)
    password_label.config(text=f"Generated Password: {password}")

def copy_to_clipboard(text):
    if "Generated Name: " in text:
        text = text.replace("Generated Name: ", "")
    elif "Generated Password: " in text:
        text = text.replace("Generated Password: ", "")
    elif "Generated Email: " in text:
        text = text.replace("Generated Email: ", "")
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Keeps the clipboard content after the window is closed
    messagebox.showinfo("Copied", "Text copied to clipboard")

def run_app(icon_path=None):
    global root, name_label, email_label, password_label, nationality_var, password_length_scale

    # Create the main window
    root = tk.Tk()
    root.title("ID GENERATOR")
    root.geometry(config.WINDOW_SIZE)  # Set the window size
    if icon_path:
        root.iconbitmap(icon_path)
    root.configure(bg=config.BACKGROUND_COLOR)

    # Create and place the labels and buttons
    name_label = tk.Label(root, text="Generated Name: ", wraplength=400, bg=config.BACKGROUND_COLOR, fg=config.FOREGROUND_COLOR)
    name_label.pack()

    email_label = tk.Label(root, text="Generated Email: ", wraplength=400, bg=config.BACKGROUND_COLOR, fg=config.FOREGROUND_COLOR)
    email_label.pack()

    password_label = tk.Label(root, text="Generated Password: ", wraplength=400, bg=config.BACKGROUND_COLOR, fg=config.FOREGROUND_COLOR)
    password_label.pack()

    generate_name_email_button = tk.Button(root, text="Generate Name and Email", command=generate_name_and_email, bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
    generate_name_email_button.pack()

    generate_password_button = tk.Button(root, text="Generate Password", command=generate_new_password, bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
    generate_password_button.pack()

    # Create and place the scale for password length
    password_length_scale = tk.Scale(root, from_=8, to_=128, orient=tk.HORIZONTAL, label="Password Length", bg=config.BACKGROUND_COLOR, fg=config.FOREGROUND_COLOR)
    password_length_scale.set(12)  # Default length
    password_length_scale.pack()

    # Add a button to copy the generated name to the clipboard
    copy_name_button = tk.Button(root, text="Copy Name", command=lambda: copy_to_clipboard(name_label.cget("text")), bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
    copy_name_button.pack()

    # Add a button to copy the generated password to the clipboard
    copy_password_button = tk.Button(root, text="Copy Password", command=lambda: copy_to_clipboard(password_label.cget("text")), bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
    copy_password_button.pack()

    # Add a button to copy the generated email to the clipboard
    copy_email_button = tk.Button(root, text="Copy Email", command=lambda: copy_to_clipboard(email_label.cget("text")), bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
    copy_email_button.pack()

    # Create and place the option menu for nationality selection
    nationality_var = tk.StringVar(root)
    nationality_var.set("us")  # Default value

    nationality_label = tk.Label(root, text="Select Nationality:", bg=config.BACKGROUND_COLOR, fg=config.FOREGROUND_COLOR)
    nationality_label.pack()

    nationality_menu = tk.OptionMenu(root, nationality_var, "us", "es", "gb", "ru")
    nationality_menu.config(bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
    nationality_menu.pack()

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    run_app()