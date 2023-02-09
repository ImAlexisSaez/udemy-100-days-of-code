from data import MENU, resources


def is_resource_sufficient(order_ingredients):
    """Returns True if there are enough ingredients. False otherwise."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("\tHow many quarters? ")) * 0.25
    total += int(input("\tHow many dimes? ")) * 0.1
    total += int(input("\tHow many nickels? ")) * 0.05
    total += int(input("\tHow many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"\tHere is ${change} in change.")
        profit += drink_cost
        return True
    else:
        print("\tSorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\tHere is your {drink_name}.")


is_on = True
profit = 0

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"\tWater: {resources['water']} ml")
        print(f"\tMilk: {resources['milk']} ml")
        print(f"\tCoffee: {resources['coffee']} g")
        print(f"\tMoney: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink['ingredients'])


