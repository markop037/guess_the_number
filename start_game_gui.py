import tkinter as tk
from tkinter import messagebox
from guess_number_gui import GuessNumber
from guess_number_db import check_username_exists


class StartWindow:
    def __init__(self, master):
        self.master = master
        master.configure(background="Orange")
        master.title("Guess My Number Game")
        self.username = None

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x = (screen_width // 2) - (350 // 2)
        y = (screen_height // 2) - (250 // 2)

        self.master.geometry(f'{350}x{250}+{x}+{y}')

        self.welcome_label = tk.Label(master, text="Welcome to Guess My Number Game",
                                      font=("Arial", 15), background="Orange")
        self.welcome_label.pack(pady=30)

        self.username_label = tk.Label(master, text="Enter your username:", font=("Arial", 10), background="Orange")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_game, font=("Arial", 11),
                                      background="dodger blue")
        self.start_button.pack(pady=10)

    def start_game(self):
        username = self.username_entry.get() if self.username_entry.get() else "Guest"

        if username != "Guest" and check_username_exists(username):
            messagebox.showerror("Error", "Username already exists! Please choose a different one.")

        else:
            self.username = username
            self.master.destroy()
            self.open_game_window()

    def open_game_window(self):
        game_root = tk.Tk()
        game_app = GuessNumber(game_root, self.username)
        game_root.mainloop()
