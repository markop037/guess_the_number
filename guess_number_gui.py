import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import time
from guess_number_db import *


class GuessNumber:
    def __init__(self, master, username):
        self.master = master
        master.configure(background="Orange")
        master.title("Guess My Number Game")
        self.username = username

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x = (screen_width // 2) - (350 // 2)
        y = (screen_height // 2) - (250 // 2)

        self.master.geometry(f'{350}x{250}+{x}+{y}')

        self.min_number = 1
        self.max_number = 100
        self.number_to_guess = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.start_time = time.time()

        self.guess_label = tk.Label(master, text=f"Enter a number between {self.min_number} and {self.max_number}:",
                                    font=("Arial", 10), background="Orange")
        self.guess_label.pack(pady=10)
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.check_number, font=("Arial", 11),
                                       background="dodger blue")
        self.submit_button.pack(pady=10)

        self.buttom_frame = tk.Frame(master)
        self.buttom_frame.config(background="Orange")

        self.reset_buttom = tk.Button(self.buttom_frame, text="Reset", command=self.reset_game, font=("Arial", 11),
                                      background="dodger blue")
        self.reset_buttom.grid(row=0, column=0, padx=15, pady=10)

        self.show_result = tk.Button(self.buttom_frame, text="Results", command=self.show_results, font=("Arial", 11),
                                     background="dodger blue")
        self.show_result.grid(row=0, column=1, padx=15, pady=10)

        self.buttom_frame.pack()

        self.result_label = tk.Label(master, text="", background="Orange")
        self.result_label.pack()

    def reset_game(self):
        print(f"Debug: Number to guess is {self.number_to_guess}")
        self.number_to_guess = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.start_time = time.time()
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)

    def check_number(self):
        try:
            user_number = int(self.guess_entry.get())
            self.attempts += 1
            if user_number < self.number_to_guess:
                self.result_label.config(text="Your number is too low. Try again.")
            elif user_number > self.number_to_guess:
                self.result_label.config(text="Your number is too high. Try again.")
            else:
                time_taken = time.time() - self.start_time
                save_score(self.username, self.attempts, time_taken)
                messagebox.showinfo("Congratulations",
                                    f"{self.username}, you've guessed the number {self.number_to_guess} "
                                    f"in {self.attempts} attempts and {time_taken:.2f} seconds!")

                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

    def show_results(self):
        rows = open_database()

        result_window = tk.Toplevel(self.master)
        result_window.title("Scores")

        tree = ttk.Treeview(result_window, columns=("Username", "Attempts", "TimeTaken", "DatePlayed"), show="headings")
        tree.heading("Username", text="Username")
        tree.heading("Attempts", text="Attempts")
        tree.heading("TimeTaken", text="Time Taken")
        tree.heading("DatePlayed", text="Date Played")
        tree.pack(fill=tk.BOTH, expand=True)

        tree.tag_configure('evenrow', background='#f0f0f0')
        tree.tag_configure('oddrow', background='#ffffff')

        for i, row in enumerate(rows):
            date_played = row.DatePlayed.strftime("%Y-%m-%d %H:%M:%S")

            if i % 2 == 0:
                tree.insert("", tk.END, values=(row.Username, row.Attempts, round(row.TimeTaken, 2), date_played),
                            tags=('evenrow',))
            else:
                tree.insert("", tk.END, values=(row.Username, row.Attempts, round(row.TimeTaken, 2), date_played),
                            tags=('oddrow',))
