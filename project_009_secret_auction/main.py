import os
from art import logo

# Limpia terminal
os.system("cls")

# Imprime logo e introducción
print(logo)

# Flag para continuar subasta
continue_auction = True
auction_bidders = {}

while continue_auction:
    name = input("What is your name? ").lower()
    bid = int(input("What's your bid? $"))

    auction_bidders[name] = bid

    next_bidder = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if next_bidder == 'yes':
        os.system("cls")
    elif next_bidder == 'no':
        winner = ""
        max_bid = -1
        for bidder, bid in auction_bidders.items():
            if bid > max_bid:
                winner = bidder
                max_bid = bid

        os.system("cls")
        print(f"The winner is {winner} with a bid of ${bid}.")
        continue_auction = False
