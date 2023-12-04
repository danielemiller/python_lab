# number_guessing_game_v2.py

import random

def generate_number(min_val, max_val):
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

def main():
    min_val = 1
    max_val = 100
    max_attempts = 10

    target_number = generate_number(min_val, max_val)
    attempts = 0

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        result = check_guess(guess, target_number)
        print(result)

        if result == "Correct!":
            print(f"You guessed the number in {attempts} attempts!")
            score = calculate_score(attempts, max_attempts)
            print(f"Your score: {score}")
            break
    else:
        print(f"Sorry, you didn't guess the number. It was {target_number}.")

if __name__ == "__main__":
    main()
