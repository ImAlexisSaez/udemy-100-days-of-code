from art import logo
import os


def caesar(start_text, shift_amount, cipher_direction):

    if cipher_direction == "decode":
        shift_amount *= -1

    end_text = ""

    for letter in start_text:
        # Solo codifica/decodifica letras. 
        # Números, símbolos y espacios quedan igual.
        if letter.isalpha():  # Alternativa: if letter in alphabet
            index = alphabet.index(letter)
            end_text += alphabet[(index + shift_amount) % 26]
        else:
            end_text += letter

    print(f"The {cipher_direction}d text is {end_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Limpia pantalla
os.system("cls")
print(logo)

use_caesar = True

while use_caesar:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    user_input = input("Type 'yes' to use again the app, and 'no' to quit. ").lower()

    if user_input == "no":
        print("Goodbye!")
        use_caesar = False
