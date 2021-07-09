def encrypt(plain_text, shift_amount):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    encrypt_text = ''
    for char in plain_text:
        index = (alphabet.index(char) + shift_amount) % len(alphabet)
        encrypt_text += alphabet[index]
    print(f"The encoded text is:\n🔏 {encrypt_text} 🔏")


def decrypt(encrypt_text, shift_amount):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    plain_text = ''
    for char in encrypt_text:
        index = (alphabet.index(char) - shift_amount) % len(alphabet)
        plain_text += alphabet[index]
    print(f"The decoded text is:\n🔏 {plain_text} 🔏")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
else:
    decrypt(text, shift)

