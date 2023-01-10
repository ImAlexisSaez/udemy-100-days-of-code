"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
"""


def turn_right():
    for i in range(3):
        turn_left()


while not at_goal():
    if wall_in_front():
        # sube
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        # baja
        turn_right()
        move()
        while front_is_clear():
            move()
        turn_left()
    else:
        move()
