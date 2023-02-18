from alphabet import alphabet
from caesar_art import logo

print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))


    def caesar(plain_text, shift_amount, left_or_right):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            if left_or_right == "encode":
                new_position = position + shift_amount
            else:
                new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        if left_or_right == "encode":
            print(f"The encoded text is {cipher_text}")
        else:
            print(f"The decoded text is {cipher_text}")


    caesar(plain_text=text, shift_amount=shift, left_or_right=direction)

    result = input("Type 'y' to go again, type 'n' to leave: ")
    if result == "n":
        should_continue = False
        print("\nGoodbye")
