import random

class GuessNumber:
    def __init__(self, min_number=1, max_number=100):
        self.min_number = min_number
        self.max_number = max_number
        self.number_to_guess = random.randint(self.min_number, self.max_number)
        self.attempts = 0

    def reset_game(self):
        self.number_to_guess = random.randint(self.min_number, self.max_number)
        self.attempts = 0

    def check_number(self, user_number):
        self.attempts += 1
        if user_number < self.number_to_guess:
            return "Your number is too low. Try again."
        elif user_number > self.number_to_guess:
            return "Your number is too high. Try again."
        else:
            return f"Congratulations! You've guessed the number {self.number_to_guess} in {self.attempts} attempts."

    def play(self):
        print("Welcome to the 'Guess the Number' game!")
        name = input("Enter your name: ")

        while True:
            user_input = input(f"Enter a number between {self.min_number} and {self.max_number}: ")

            try:
                user_number = int(user_input)
            except ValueError:
                print("Please enter a valid number.")
                continue

            result = self.check_number(user_number)
            print(result)

            if user_number == self.number_to_guess:
                break

if __name__ == "__main__":
    game = GuessNumber()
    game.play()
