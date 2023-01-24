import random

import v41_02

print(v41_02.pi)

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float_5 = 5 * random.random()
print(random_float_5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")
