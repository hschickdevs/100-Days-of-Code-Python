import random

import art


def get_lives():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return 10
    if level == 'hard':
        return 5
    print("🤬 You entered a invalid difficulty, I'm choosing for you. 🤬")
    return random.choice([5, 10])


def check_answer(guess, answer, lives):
    """Give the user a feedback on his
    guess. Returns if guess == answer"""
    if guess == answer:
        print("\n🎉 You got it! 🎉")
        return True
    if lives == 1:
        print("\n👻 You've ran out of guesses. You lose! 👻")
    elif guess < answer:
        print("Too low. Guess again!")
    else:
        print("Too high. Guess again!")
    return False


def game():
    print(art.logo)
    print("🔮 Welcome to the Number Guessing Game! 🔮")
    print("🤔 I'm thinking of a number between 1 and 100. 🤔")

    secret_number = random.randint(1, 100)

    # Test code
    # print(f'\nPssst, the correct answer is: {secret_number}\n')

    for lives in range(get_lives(), 0, -1):
        print(f"\nYou have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if check_answer(guess, secret_number, lives):
            break
    print(f"The answer was: {secret_number}!")


game()
