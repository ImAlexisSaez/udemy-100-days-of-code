import os
import random

from art import logo, vs
from game_data import data


def choose_option(data_list):
    """Escoge un elemento al azar de una lista y lo borra para evitar repeticiones.

    Args:
        data_list (list): lista de datos (lista de diccionarios).

    Returns:
        dict: diccionario escogido de la lista inicial.
    """
    random_index = random.randrange(len(data_list))
    option = data_list[random_index]
    del data_list[random_index]
    return option


def print_comparation(first_option, second_option):
    """Imprime en pantalla la comparación de opciones.

    Args:
        first_option (dict): diccionario con los datos de la primera opción.
        second_option (dict): diccionario con los datos de la segunda opción.
    """
    os.system("cls")
    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}.")
    print(
        f"Compare A: {first_option['name']}, ",
        f"{first_option['description']}, ",
        f"from {first_option['country']}."
    )
    print(vs)
    print(
        f"Compare B: {second_option['name']}, ",
        f"{second_option['description']}, "
        f"from {second_option['country']}."
    )


def is_guess_right(guess, first_option, second_option):
    """Devuelve True si el jugador acertó, False en otro caso.

    Args:
        guess (str): opción dle jugador
        first_option (dict): diccionario con los datos de la primera opción.
        second_option (dict): diccionario con los datos de la segunda opción.

    Returns:
        bool: True si acertó, False si fallo.
    """
    if first_option['follower_count'] > second_option['follower_count'] and guess == 'a':
        return True
    elif first_option['follower_count'] < second_option['follower_count'] and guess == 'b':
        return True
    else:
        return False


def game_over_screen(score):
    """Imprime pantalla de despedida con la puntuación final.

    Args:
        score (int): puntuación del jugador.
    """
    os.system("cls")
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}.")


# Variables globales:
score = 0
right_guess = True

# Selecciona aleatoriamente dos opciones a comparar de data:
option_a = choose_option(data)
option_b = choose_option(data)

while right_guess:
    # Imprime pantalla:
    print_comparation(option_a, option_b)

    # Debugging:
    # print(f"A: {option_a['follower_count']}; B: {option_b['follower_count']}")

    # Pide respuesta
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if is_guess_right(guess, option_a, option_b):
        score += 1
        if option_b['follower_count'] > option_a['follower_count']:
            option_a = option_b
        option_b = choose_option(data)
    else:
        game_over_screen(score)
        right_guess = False
