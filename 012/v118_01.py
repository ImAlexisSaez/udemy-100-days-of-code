# Modifying global scope
enemies = 1


def increase_enemies():
    # No es recomendable modificar variables globales... pero en caso de querer hacerlo.
    global enemies  # Ahora sí podemos modificar la variable con scope global.
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
