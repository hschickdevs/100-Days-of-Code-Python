import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
display = ['_'] * len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

while '_' in display:
    print(display)
    guess = input("Guess a letter: ").lower()
    for idx, letter in enumerate(chosen_word):
        if guess == letter:
            display[idx] = letter
print(display)
print("You win!")
