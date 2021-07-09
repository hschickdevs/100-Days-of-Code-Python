###############     Blackjack Project      ####################
############### Our Blackjack House Rules: ####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
from art import cardUI
import random

game_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10,
             10, "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King",
             "Ace", "Ace", "Ace", "Ace"]

player_deck = []
player_score = 0
dealer_deck = []
dealer_score = 0
bet = 0
play = True

print(logo)
print()
print("Welcome to Blackjack!")
chips = int(input("How many chips do you want to start with: "))


def draw(whodeck, whoscore):
    draw = str(random.choice(game_deck))
    whodeck.append(draw)
    if draw == "Jack":
        whoscore += 10
    elif draw == "Queen":
        whoscore += 10
    elif draw == "King":
        whoscore += 10
    elif draw == "Ace":
        if input("Ace! Do you want it to be a 1 or 11?") == "1":
            whoscore += 1
        else:
            whoscore += 11
    else:
        whoscore += int(draw)


def gameinit():
    random.shuffle(game_deck)
    draw(dealer_deck, dealer_score)
    for _ in range(2):
        draw(player_deck, player_score)


while play:
    bet = int(input("What is your bet for this game: "))
    print(f"\nPress 'Enter' to start the game with {chips} chips remaining and a bet of {bet} chips.")
    if bet <= chips:
        chips -= bet
        gameinit()
        cardUI(player_deck, chips, bet)

    else:
        print(f"You only have {chips} chips. You can't bet {bet}.\n")
