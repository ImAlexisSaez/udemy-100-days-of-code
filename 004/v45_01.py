states_of_america = ["Delaware", "Pennsylvania"]

print(states_of_america[0])
print(states_of_america[1])
print(states_of_america[-1])
print(states_of_america[-2])

states_of_america[1] = "Pencilvania"
print(states_of_america)

states_of_america.append("New Jersey")
print(states_of_america)

states_of_america.extend(["Virginia", "New York"])
print(states_of_america)

print(len(states_of_america))

# print(states_of_america[5])  # IndexError