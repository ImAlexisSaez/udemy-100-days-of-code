from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_machine = CoffeeMaker()
menu_machine = Menu()
profit = MoneyMachine()

while is_on:
    choice = input(f"What would you like? ({menu_machine.get_items()}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
    else:
        drink = menu_machine.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if profit.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
