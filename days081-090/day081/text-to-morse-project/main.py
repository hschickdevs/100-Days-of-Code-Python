import json
import os

db_location = os.path.join(os.getcwd(), 'morse_db.json')

overwrite_db = True
if not os.path.exists(db_location) or overwrite_db:
    with open(db_location, 'w') as outfile:
        morse_database = {
            "0": "----- ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "----. ",
            "a": ".- ",
            "b": "-... ",
            "c": "-.-. ",
            "d": "-.. ",
            "e": ". ",
            "f": "..-. ",
            "g": "--. ",
            "h": ".... ",
            "i": ".. ",
            "j": ".--- ",
            "k": "-.- ",
            "l": ".-.. ",
            "m": "-- ",
            "n": "-. ",
            "o": "--- ",
            "p": ".--. ",
            "q": "--.- ",
            "r": ".-. ",
            "s": "... ",
            "t": "- ",
            "u": "..- ",
            "v": "...- ",
            "w": ".-- ",
            "x": "-..- ",
            "y": "-.-- ",
            "z": "--.. ",
            ".": ".-.-.- ",
            ",": "--..-- ",
            "?": "..--.. ",
            "!": "-.-.-- ",
            "-": "-....- ",
            "/": "-..-. ",
            "@": ".--.-. ",
            "(": "-.--. ",
            ")": "-.--.- ",
            " ": "/ "
        }
        json.dump(morse_database, outfile, indent=2)


def text_to_morse(user_message, database_location) -> str:
    with open(database_location) as infile:
        morse_db = json.load(infile)

    morsed_message = ""
    for char in user_message.lower():
        try:
            morsed_message += morse_db[char]
        except KeyError:
            morsed_message += char

    return morsed_message


if __name__ == "__main__":
    user_message = input('Enter message to be converted to morse code:\n')
    print(text_to_morse(user_message=user_message, database_location=db_location))
