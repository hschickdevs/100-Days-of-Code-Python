import json
import os

db_location = os.path.join(os.getcwd(), 'morse_db.json')

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
