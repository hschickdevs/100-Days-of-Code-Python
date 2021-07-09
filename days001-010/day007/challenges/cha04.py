import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

while '_' in display and lives > 0:
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if guess == letter:
                display[idx] = letter
    else:
        lives -= 1
    print(stages[lives])
print(f"{' '.join(display)}")

if lives == 0:
    print("You lose!")
else:
    print("You win!")
