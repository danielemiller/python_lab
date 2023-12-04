import random

def generate_number(min_val, max_val):
    # Generates a random number between min_val and max_val
    return random.randint(min_val, max_val)

def get_guess():
    # Gets user's guess and handles invalid inputs
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")

def check_guess(guess, target):
    # Checks the guess against the target number and returns feedback
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

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
            break
    else:
        print(f"Sorry, you didn't guess the number. It was {target_number}.")

if __name__ == "__main__":
    main()
