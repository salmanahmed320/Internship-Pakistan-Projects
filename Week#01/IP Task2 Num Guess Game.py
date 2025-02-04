# INTERNSHIP PAKISTAN
# TASK_2
# Create a number-guessing game where the user tries to guess a randomly generated number between 1 and 100.
 
import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            # Prompt the user to enter a guess
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            # Check if the guess is correct, too high, or too low
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Run the game
number_guessing_game()
