import tkinter as tk
from tkinter import messagebox
import random
import time
from guess_number_db import save_score


class GuessNumber:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number Game")

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

        self.username_label = tk.Label(master, text="Enter your username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.guess_label = tk.Label(master, text=f"Enter a number between {self.min_number} and {self.max_number}:")
        self.guess_label.pack()
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_number)
        self.submit_button.pack()

        self.reset_buttom = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_buttom.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def reset_game(self):
        print(f"Debug: Number to guess is {self.number_to_guess}")
        self.number_to_guess = random.randint(self.min_number, self.max_number)
        self.attempts = 0
        self.start_time = time.time()
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)

    def check_number(self):
        try:
            user_number = int(self.guess_entry.get())
            self.attempts += 1
            if user_number < self.number_to_guess:
                self.result_label.config(text="Your number is too low. Try again.")
            elif user_number > self.number_to_guess:
                self.result_label.config(text="Your number is too high. Try again.")
            else:
                username = self.username_entry.get() if self.username_entry.get() else "Guest"
                time_taken = time.time() - self.start_time
                save_score(username, self.attempts, time_taken)
                messagebox.showinfo("Congratulations",
                                    f"{username}, you've guessed the number {self.number_to_guess} "
                                    f"in {self.attempts} attempts and {time_taken:.2f} seconds!")

                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")