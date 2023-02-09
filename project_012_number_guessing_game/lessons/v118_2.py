# Alternativa para modificar variables globales.
# Usar return.

def increase_enemies():
    return enemies + 1


enemies = 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")
