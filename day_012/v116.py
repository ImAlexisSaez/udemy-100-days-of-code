################### Scope ####################

enemies = 1


def increase_enemies():
    # Las funciones tienen scope local.
    enemies = 2  # Nueva variable, no es el enemies de arriba.
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength)  # NameError

# Global scope
player_health = 10


def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()
