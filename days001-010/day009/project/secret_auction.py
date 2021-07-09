import os

import art


def get_max(bids_dict):
    max_bid = 0
    max_bidder = ''
    for bidder, bid_amount in bids_dict.items():
        if bid_amount > max_bid:
            max_bid = bid_amount
            max_bidder = bidder
    print(f"The winner is '{max_bidder}' with a bid of: ${max_bid:.2f}")


bids = {}
more_bids = 'yes'
while more_bids == 'yes':
    print(art.logo)
    print("Welcome to the Secret Action Program!\n")

    name = input("What's your name? ")
    bid = float(input("What's your bid? $"))
    bids[name] = bid

    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
get_max(bids)

