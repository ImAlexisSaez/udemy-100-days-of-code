# Calculator

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# Dict with operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number? "))

for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation from the line above: ").lower()

num2 = int(input("What's the next number? "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

user_continue = input(
    f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()

if user_continue == 'y':
    continue_calculating = True
elif user_continue == 'n':
    continue_calculating = False

while continue_calculating:
    num1 = answer
    operation_symbol = input("Pick an operation from the line above: ").lower()
    num2 = int(input("What's the next number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    user_continue = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ").lower()

    if user_continue == 'y':
        continue_calculating = True
    elif user_continue == 'n':
        continue_calculating = False
