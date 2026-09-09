import tkinter as tk

window = tk.Tk()
window.title("My Playlist")
window.geometry("500x300")
label = tk.Label(
    window,
    text="Welcome to Your Music Playlist"
)
label.pack()
window.mainloop()