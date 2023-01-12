# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")


# Llamadas con argumentos posicionales
greet_with("Alexis", "Ibi")
greet_with("Ana", "Elche")

# Llamadas con key-word
greet_with(name="Alexis", location="Ibi")
greet_with(location="Elche", name="Ana")
