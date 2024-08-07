import tkinter as tk
from tkinter import messagebox
import random


class GuessNumber:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number Game")

        self.min_number = 1
        self.max_number = 100
        self.number_to_guess = random.randint(self.min_number, self.max_number)
        self.attempts = 0

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
                self.result_label.config(text=f"Congratulations! {self.username_entry.get()}, "
                                              f"you've guessed the number {self.number_to_guess} "
                                              f"in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")