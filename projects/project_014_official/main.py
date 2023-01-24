import random
import os

from art import logo, vs
from game_data import data

def format_data(account):
    """Format the account data into printable format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Check if the user is correct."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    # Display art.
    print(logo)

    # Making account at position B become next account at position A

    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)


    # Format the account data into printable format.
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    # Check if user is correct.
    ## Get follower count of each account.
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    os.system("cls")
    print(logo)

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")






# Make the game repeatable.



# Clear the screen between rounds.