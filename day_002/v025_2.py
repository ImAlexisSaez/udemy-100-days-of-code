# Solución oficial
age = input("What is your current age? ")

age_as_int = int(age)

years_remainig = 90 - age_as_int

days_remaining = years_remainig * 365
weeks_remaining = years_remainig * 52
months_remaining = years_remainig * 12

message = f"You have {days_remaining}, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
