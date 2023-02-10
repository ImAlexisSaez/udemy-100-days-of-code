numbers = [1, 2, 3]

numbers_1 = [n + 1 for n in numbers]
print(numbers_1)

name = "Angela"
letters_name = [letter for letter in name]
print(letters_name)

doubled_numbers = [2 * i for i in range(1, 5)]
print(doubled_numbers)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_cap_names = [name.upper() for name in names if len(name) > 5]
print(long_cap_names)
