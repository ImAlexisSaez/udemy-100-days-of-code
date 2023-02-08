"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
"""


def turn_right():
    for i in range(3):
        turn_left()


def move_n(n):
    for i in range(n):
        move()


def up():
    move()
    turn_left()
    move()
    turn_right()


def down():
    move()
    turn_right()
    move()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    jump()
