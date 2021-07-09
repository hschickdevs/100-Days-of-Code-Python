from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine(menu, coffee_maker, money_machine):
    drink_name = input(f"What would you like? ({menu.get_items()}\b): ")
    if drink_name == 'off':
        return
    if drink_name == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(drink_name)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    coffee_machine(menu, coffee_maker, money_machine)


def machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    coffee_machine(menu, coffee_maker, money_machine)


machine()
