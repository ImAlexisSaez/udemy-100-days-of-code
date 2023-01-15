import random
import os

from art import logo


def guess_the_number():
    # Presentación del juego
    os.system("cls")  # Limpia terminal

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Cálculo del número a adivinar
    solution = random.randint(1, 100)
    # print(f"\tSolution: {solution} (for debugging)")  # Debugging

    # Selección de dificultad
    choosing_difficulty = False
    while not choosing_difficulty:
        difficulty = input(
            "Choose a difficulty. Type 'easy' or 'hard': ").lower()

        if difficulty == 'hard':
            attempts = 5
            choosing_difficulty = True
        elif difficulty == 'easy':
            attempts = 10
            choosing_difficulty = True
        else:
            print("\tInvalid option. Please read carefully.")

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
