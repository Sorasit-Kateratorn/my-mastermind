import random

# class MastermindGame


class MastermindGame:
    def __init__(self, num_colors, num_positions):
        self.num_colors = num_colors
        self.num_positions = num_positions
        self.__secret_code = [random.randint(
            1, num_colors) for _ in range(num_positions)]

    def check_guess(self, guess):
        clues = []
        for i in range(self.num_positions):
            if guess[i] == self.__secret_code[i]:
                clues.append('*')
            elif guess[i] in self.__secret_code:
                clues.append('o')
            else:
                clues.append(' ')
        return ''.join(clues)

# min_value and max_value is the scope for solve error from int(num_colors) and int(num_positions)


def get_numeric_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(
                    f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# main function


def play_mastermind():
    num_colors = get_numeric_input("Enter the number of colors (1-8): ", 1, 8)
    num_positions = get_numeric_input(
        "Enter the number of positions (1-10): ", 1, 10)
    print(
        f"Playing Mastermind with {num_colors} colors and {num_positions} positions")

    game = MastermindGame(num_colors, num_positions)

    round_count = 0
    while True:
        round_count += 1
        guess = input("What is your guess?: ")[:num_positions]
        print(f"Your guess is {guess}")

        if len(guess) != num_positions or not guess.isdigit():
            print("Invalid input. Please enter a valid guess.")
            continue

        guess = [int(digit) for digit in guess]

        result = game.check_guess(guess)
        print(result)

        if result == '*' * num_positions:
            print(f"You solved it after {round_count} rounds")
            break


if __name__ == "__main__":
    print("Welcome to Mastermind game!")
    play_mastermind()
