# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode="r") as file:
    starting_letter = file.readlines()

with open("Input/Names/invited_names.txt", mode="r") as file:
    invited_names = file.readlines()

invited_names = [name.strip() for name in invited_names]

for name in invited_names:
    new_letter = starting_letter.copy()
    new_letter[0] = new_letter[0].replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}", mode="w") as file:
        file.writelines(new_letter)
