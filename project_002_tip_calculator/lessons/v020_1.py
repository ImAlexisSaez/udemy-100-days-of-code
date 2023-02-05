# len(483)  # TypeError

num_char = len(input("What is your name? "))
# print("Your name has " + num_char + " characters.")  # TypeError

print(type(num_char))  # type indica el tipo de objeto.

# Type casting (or type conversion)
print("Your name has " + str(num_char) + " characters.")

# Alternativa
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
