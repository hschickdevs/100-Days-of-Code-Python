import pandas as pd


def generate_nato():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the english alphabet, please.")
        generate_nato()
    else:
        print(nato_list)


df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for index, row in df.iterrows()}

generate_nato()
