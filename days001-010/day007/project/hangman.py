import os
import random

import art
import words


chosen_word = random.choice(words.word_list)
display = ['_'] * len(chosen_word)
lives = 6
guessed_letters = []

print(art.logo)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

print(f"{' '.join(display)}")
while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    if guess in guessed_letters:
        print(f"You already tried the letter '{guess.upper()}'")
    else:
        if guess in chosen_word:
            for idx, letter in enumerate(chosen_word):
                if guess == letter:
                    display[idx] = letter
        else:
            print(f"The letter '{guess.upper()}' is not in the chosen word. You lose a life!")
            lives -= 1
    guessed_letters.append(guess)
    print(art.stages[lives])
    print(f"{' '.join(display)}")

print(f"The word was: '{chosen_word.upper()}'")
if lives == 0:
    print("You lose!")
else:
    print("You win!")
