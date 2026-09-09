import tkinter as tk

window = tk.Tk()

window.title("Social Media")
window.geometry("400x300")

like_button = tk.Button(window, text="Like")
like_button.grid(row=0, column=0, padx=20, pady=20)

share_button = tk.Button(window, text="Share")
share_button.grid(row=0, column=1, padx=20, pady=20)

download_button = tk.Button(window, text="Download")
download_button.grid(row=1, column=0, padx=20, pady=20)

queue_button = tk.Button(window, text="Add to Queue")
queue_button.grid(row=1, column=1, padx=20, pady=20)
window.mainloop()