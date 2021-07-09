import os
import random

import art
import game_data


def compare(a_followers, b_followers, choice):
    if choice == 'a':
        return a_followers >= b_followers
    return b_followers >= a_followers


def format_entry(entry):
    name = entry['name']
    desc = entry['description']
    country = entry['country']
    return f'{name}, a(n) {desc}, from {country}.'


def higher_lower(data, score, a):
    b = random.choice(data)
    data.remove(b)

    print(f'Compare A: {format_entry(a)}')
    print(art.vs)
    print(f'Against B: {format_entry(b)}')

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')

    print(art.logo)
    if not compare(a['follower_count'], b['follower_count'], choice):
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        score += 1
        print(f"You are right! Current score: {score}")
        a = b
        if len(data) == 0:
            data = game_data.data
            data.remove(a)
        higher_lower(data, score, a)


def game():
    data = game_data.data
    a = random.choice(data)
    data.remove(a)
    print(art.logo)
    higher_lower(data, 0, a)


game()
