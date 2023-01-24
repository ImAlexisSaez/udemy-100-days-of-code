# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What vas the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

pay_per_person = round((bill / number_of_people) * (1 + tip / 100), 2)
print(f"Each person should pay: ${pay_per_person}")

# Problema con mi solución: si el resultado no tiene dos o más números
# decimales, no muestra dos posiciones decimales. Solo el resultado.
# Hay que usar reglas de formato. Mirar la solución oficial.

# Solución oficial
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")
