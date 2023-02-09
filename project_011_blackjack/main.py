import random
import os

from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)
    if score == 21:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score


def blackjack():
    os.system("cls")
    print(logo)

    user_cards = []
    computer_cards = []

    user_cards.extend([deal_card(), deal_card()])
    computer_cards.extend([deal_card(), deal_card()])

    user_playing = True
    computer_playing = True
    while user_playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\tYour cards: {user_cards}, current score: {user_score}.")
        print(f"\tComputer's first card: {computer_cards[0]}")

        if user_score == 0:
            user_playing = False
            computer_playing = False
            print("\n\tBlackjack! User wins!")
        elif computer_score == 0:
            user_playing = False
            computer_playing = False
            print("\n\tBlackjack! Computer wins!")
        elif user_score > 21:
            user_playing = False
            computer_playing = False
            print("\n\tUser is over 21. User loses!")
        else:
            another_card = input(
                "Do you want another card? ('y' or 'n') ").lower()
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                user_playing = False

    # Juega pc
    while computer_playing:
        while computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        if computer_score > 21:
            computer_playing = False
            print(
                f"\tComputer cards: {computer_cards}, current score: {computer_score}.")
            print("\n\tComputer is over 21. User wins!")
        else:
            if computer_score == user_score:
                computer_playing = False
                print(
                    f"\tComputer cards: {computer_cards}, current score: {computer_score}.")
                print("\n\tIt's a draw!")
            elif computer_score > user_score:
                computer_playing = False
                print(
                    f"\tComputer cards: {computer_cards}, current score: {computer_score}.")
                print("\n\tComputer wins!")
            else:
                computer_playing = False
                print(
                    f"\tComputer cards: {computer_cards}, current score: {computer_score}.")
                print("\n\tUser wins")


while True:
    game = input(
        "Do you want to play a game of Blackjack? ('y' or 'n') ").lower()
    if game == 'y':
        blackjack()
    else:
        break
