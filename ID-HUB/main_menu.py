import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random_name_generator
import person_search
import config

def open_random_name_generator():
    random_name_generator.run_app(icon_path=config.WINDOW_ICON)

def open_person_search():
    person_search.run_app(icon_path=config.WINDOW_ICON)

# Create the main window
root = tk.Tk()
root.title("ID-HUB")
root.geometry(config.WINDOW_SIZE)  # Set the window size
root.iconbitmap(config.WINDOW_ICON)
root.configure(bg=config.BACKGROUND_COLOR)

# Load the background image
background_image = Image.open(config.BACKGROUND_IMAGE)
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas to display the background image
canvas = tk.Canvas(root, width=800, height=600, bg=config.BACKGROUND_COLOR)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")


# Create and place the buttons
open_generator_button = tk.Button(root, text="ID Generator", command=open_random_name_generator, bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
open_generator_button_window = canvas.create_window(400, 200, anchor="center", window=open_generator_button)

open_person_search_button = tk.Button(root, text="Hunter.io search", command=open_person_search, bg=config.BUTTON_BG_COLOR, fg=config.BUTTON_FG_COLOR)
open_person_search_button_window = canvas.create_window(400, 300, anchor="center", window=open_person_search_button)

root.mainloop()