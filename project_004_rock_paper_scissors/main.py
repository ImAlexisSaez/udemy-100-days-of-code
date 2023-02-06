import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
opciones = [0, 1, 2]
imagenes = [rock, paper, scissors]

prompt = "What do you choose?\n"
prompt += "Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"

eleccion_jugador = int(input(prompt))

if eleccion_jugador not in opciones:
    print("Invalid number. You lose!")
else:
    print(imagenes[eleccion_jugador])

    print("\nComputer chose:")
    eleccion_pc = random.choice(opciones)
    print(imagenes[eleccion_pc])

    if eleccion_jugador == eleccion_pc:
        print("It's a draw!")
    elif eleccion_jugador == 0 and eleccion_pc == 1:
        print("You lose!")
    elif eleccion_jugador == 1 and eleccion_pc == 2:
        print("You lose!")
    elif eleccion_jugador == 2 and eleccion_pc == 0:
        print("You lose!")
    elif eleccion_jugador == 0 and eleccion_pc == 2:
        print("You win!")
    elif eleccion_jugador == 1 and eleccion_pc == 0:
        print("You win!")
    elif eleccion_jugador == 2 and eleccion_pc == 1:
        print("You win!")
