age: int
name: str
height: float
human: bool


def police_check(person_age: int) -> bool:
    if person_age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You may pass")
else:
    print("Pay a fine")