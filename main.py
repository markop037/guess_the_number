import tkinter as tk
from guess_number_gui import GuessNumber

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessNumber(root)
    root.mainloop()
