with open('Input/Letters/starting_letter.txt') as file:
    template_letter = file.read()

with open('Input/Names/invited_names.txt') as file:
    names = file.read().split()

letters = {}
for name in names:
    letters[f'letter_for_{name}'] = template_letter.replace('[name]', name)

for filename, letter in letters.items():
    with open(f'Output/ReadyToSend/{filename}.txt', mode='w') as file:
        file.write(letter)


