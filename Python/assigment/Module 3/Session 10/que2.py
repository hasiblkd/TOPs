import tkinter as tk

window = tk.Tk()

window.title("My Playlist")
window.geometry("500x300")

def play():
    status_label.config(text="Playing")

def pause():
    status_label.config(text="Paused")

def next_song():
    status_label.config(text="Next Song")

title_label = tk.Label(
    window,
    text="Welcome to Your Music Playlist"
)
title_label.pack(pady=20)
play_button = tk.Button(window, text="Play", command=play)
play_button.pack()
pause_button = tk.Button(window, text="Pause", command=pause)
pause_button.pack()
next_button = tk.Button(window, text="Next", command=next_song)
next_button.pack()
status_label = tk.Label(window, text="Select an action")
status_label.pack(pady=20)
window.mainloop()