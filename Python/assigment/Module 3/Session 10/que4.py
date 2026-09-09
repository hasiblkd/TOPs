import tkinter as tk

window = tk.Tk()

window.title("Login")
window.geometry("400x300")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username != "" and password != "":
        message_label.config(text="Login Successful")
    else:
        message_label.config(text="Please enter Username and Password")

username_label = tk.Label(window, text="Username")
username_label.pack(pady=5)
username_entry = tk.Entry(window)
username_entry.pack(pady=5)
password_label = tk.Label(window, text="Password")
password_label.pack(pady=5)
password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)
login_button = tk.Button(window, text="Login", command=login)
login_button.pack(pady=15)
message_label = tk.Label(window, text="")
message_label.pack()

window.mainloop()