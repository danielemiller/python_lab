# number_guessing_game_v4.py

import random

def generate_number(min_val, max_val, even_only=False):
    if even_only:
        return random.choice(range(min_val if min_val % 2 == 0 else min_val + 1, max_val + 1, 2))
    else:
        return random.randint(min_val, max_val)

def get_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def check_guess(guess, target):
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def calculate_score(attempts, max_attempts):
    return max(0, max_attempts - attempts + 1) * 10

def select_difficulty():
    print("Select difficulty level:\n1. Easy\n2. Medium\n3. Hard")
    while True:
        try:
            choice = int(input("Enter your choice (1, 2, 3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    difficulty = select_difficulty()
    ranges = {1: (1, 50), 2: (1, 100), 3: (1, 150)}
    min_val, max_val = ranges[difficulty]
    max_attempts = 10

    even_only = input("Should the number be even only? (yes/no): ").lower() == "yes"
    target_number = generate_number(min_val, max_val, even_only)
    attempts = 0
    past_guesses = []

    while attempts < max_attempts:
        guess = get_guess()
        past_guesses.append(guess)
        attempts += 1

        result = check_guess(guess, target_number)
        print(result)
        print("Past guesses:", past_guesses)

        if result == "Correct!":
            print(f"You guessed the number in {attempts} attempts!")
            score = calculate_score(attempts, max_attempts)
            print(f"Your score: {score}")
            break
    else:
        print(f"Sorry, you didn't guess the number. It was {target_number}.")

if __name__ == "__main__":
    main()
