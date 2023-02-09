programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

print(programming_dictionary)

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_list = []
empty_dictionary = {}

# Wipe and existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary (keys)
for thing in programming_dictionary:
    print(thing)

# Loop through a dictionary (keys)
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
