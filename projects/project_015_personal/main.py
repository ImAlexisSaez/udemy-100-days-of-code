from data import MENU, resources


def print_report():
    """Prints a report of the coffee machine."""
    print(f"\tWater: {resources['water']} ml")
    print(f"\tMilk: {resources['milk']} ml")
    print(f"\tCoffee: {resources['coffee']} g")
    print(f"\tMoney: ${money}")


def check_ingredients(order):
    """Returns True if there are enough ingredients for the order."""
    water_needed = MENU[order]['ingredients']['water']
    coffee_needed = MENU[order]['ingredients']['coffee']
    milk_needed = -1
    if 'latte' == order or 'cappuccino' == order:
        milk_needed = MENU[order]['ingredients']['milk']

    if resources['water'] < water_needed:
        print("\tSorry there is not enough water.")
        return False
    elif resources['coffee'] < coffee_needed:
        print("\tSorry there is not enough coffee.")
        return False
    elif resources['milk'] < milk_needed:
        print("\tSorry there is not enough milk.")
        return False
    else:
        return True


def ask_for_coins():
    print("\tPlease, insert coins.")
    quarters = int(input("\tHow many quarters?: "))
    dimes = int(input("\tHow many dimes?: "))
    nickels = int(input("\tHow many nickels?: "))
    pennies = int(input("\tHow many pennies?: "))
    amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies
    return amount


def use_ingredients(order, machine_money):
    machine_money += MENU[order]['cost']
    resources['water'] -= MENU[order]['ingredients']['water']
    resources['coffee'] -= MENU[order]['ingredients']['coffee']
    if 'latte' == order or 'capuccino' == order:
        resources['milk'] = MENU[order]['ingredients']['milk']
    return machine_money


is_machine_on = True
money = 0.0

while is_machine_on:
    my_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if my_order == 'off':
        is_machine_on = False
    elif my_order == 'report':
        print_report()
    else:
        if check_ingredients(my_order):
            total_coins = ask_for_coins()
            price = MENU[my_order]['cost']
            if total_coins < price:
                print("\tSorry that's not enough money. Money refunded.")
            else:
                change = total_coins - price
                if change > 0:
                    print(f"\tHere is ${change:.2f} in change.")
                money = use_ingredients(my_order, money)
                print(f"\tHere is your {my_order}. Enjoy!")
