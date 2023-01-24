"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
"""


def turn_right():
    for i in range(3):
        turn_left()


while not at_goal():
    if right_is_clear():
        turn_right()
        if front_is_clear():
            move()
    elif not right_is_clear() and front_is_clear():
        move()
    else:
        turn_left()
