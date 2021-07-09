def caesar(cipher_text, shift_amount, cipher_direction):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if cipher_direction == 'decode':
        shift_amount *= -1

    new_text = ''
    for char in cipher_text:
        index = (alphabet.index(char) + shift_amount) % len(alphabet)
        new_text += alphabet[index]
    print(f"The {cipher_direction}d text is:\n🔏 {new_text} 🔏")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(text, shift, direction)
