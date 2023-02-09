import random
import os

from art import logo

# Constants
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def _print_intro():
    os.system("cls")  # Limpia terminal

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def _set_difficulty():
    choosing_difficulty = False
    while not choosing_difficulty:
        difficulty = input(
            "Choose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty == 'hard':
            return HARD_LEVEL_ATTEMPTS
        elif difficulty == 'easy':
            return EASY_LEVEL_ATTEMPTS
        else:
            print("\tInvalid option. Please read carefully.")


def guess_the_number():
    _print_intro()

    solution = random.randint(1, 100)  # Cálculo del número a adivinar
    # print(f"\tSolution: {solution} (for debugging)")  # Debugging

    attempts = _set_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaning to guess the number.")
        guess = int(input("\tMake a guess: "))

        if guess == solution:
            print("\n\tThat's my number! You win!")
            break
        elif guess > solution:
            print("\tToo high! Guess again!")
        else:
            print("\tToo low! Guess again!")

        attempts -= 1

    if attempts == 0:
        print("\n\tYou didn't guess the number! You lose!")


os.system("cls")
start_playing = True
while start_playing:
    answer = input("Do you want to start the game? (type 'y' or 'n') ").lower()
    if answer == 'y':
        guess_the_number()
    else:
        start_playing = False
