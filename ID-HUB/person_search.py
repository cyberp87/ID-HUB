import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
import requests
import config

API_KEY = 'put your api key here'

def domain_search():
    domain = domain_entry.get()
    response = requests.get(f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={API_KEY}')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, format_response(response.json()))

def email_finder():
    domain = domain_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    response = requests.get(f'https://api.hunter.io/v2/email-finder?domain={domain}&first_name={first_name}&last_name={last_name}&api_key={API_KEY}')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, format_response(response.json()))

def email_verification():
    email = email_entry.get()
    response = requests.get(f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={API_KEY}')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, format_response(response.json()))

def company_enrichment():
    domain = domain_entry.get()
    response = requests.get(f'https://api.hunter.io/v2/company?domain={domain}&api_key={API_KEY}')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, format_response(response.json()))

def person_enrichment():
    email = email_entry.get()
    response = requests.get(f'https://api.hunter.io/v2/person?email={email}&api_key={API_KEY}')
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, format_response(response.json()))

def format_response(response):
    formatted_response = ""
    for key, value in response.items():
        formatted_response += f"{key}: {value}\n"
    return formatted_response

def run_app(icon_path=None):
    global root, domain_entry, first_name_entry, last_name_entry, email_entry, result_text

    root = tk.Tk()
    root.title("Hunter.io search")
    root.geometry(config.WINDOW_SIZE)
    if icon_path:
        root.iconbitmap(icon_path)
    root.configure(bg=config.BACKGROUND_COLOR)

    mainframe = ttk.Frame(root, padding="10 10 10 10")
    mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    ttk.Label(mainframe, text="Domain:", background=config.BACKGROUND_COLOR, foreground=config.FOREGROUND_COLOR).grid(row=0, column=0, sticky=tk.W)
    domain_entry = ttk.Entry(mainframe, width=50)
    domain_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="First Name:", background=config.BACKGROUND_COLOR, foreground=config.FOREGROUND_COLOR).grid(row=1, column=0, sticky=tk.W)
    first_name_entry = ttk.Entry(mainframe, width=50)
    first_name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="Last Name:", background=config.BACKGROUND_COLOR, foreground=config.FOREGROUND_COLOR).grid(row=2, column=0, sticky=tk.W)
    last_name_entry = ttk.Entry(mainframe, width=50)
    last_name_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="Email:", background=config.BACKGROUND_COLOR, foreground=config.FOREGROUND_COLOR).grid(row=3, column=0, sticky=tk.W)
    email_entry = ttk.Entry(mainframe, width=50)
    email_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

    ttk.Button(mainframe, text="Domain Search", command=domain_search).grid(row=4, column=0, sticky=tk.W)
    ttk.Button(mainframe, text="Email Finder", command=email_finder).grid(row=4, column=1, sticky=tk.W)
    ttk.Button(mainframe, text="Email Verification", command=email_verification).grid(row=5, column=0, sticky=tk.W)
    ttk.Button(mainframe, text="Company Enrichment", command=company_enrichment).grid(row=5, column=1, sticky=tk.W)
    ttk.Button(mainframe, text="Person Enrichment", command=person_enrichment).grid(row=6, column=0, sticky=tk.W)

    result_text = ScrolledText(mainframe, width=80, height=20, wrap=tk.WORD)
    result_text.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    mainframe.columnconfigure(1, weight=1)
    mainframe.rowconfigure(7, weight=1)

    root.mainloop()

if __name__ == "__main__":
    run_app()