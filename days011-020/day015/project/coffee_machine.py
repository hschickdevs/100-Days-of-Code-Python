def report():
    """Display a report of the amount of each
    resource and money in the coffee machine"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money:.2f}')


def check_resources(drink):
    """Check if the resources are sufficient to make the
    drink. If they are not display a message saying so to
    the user and returns False, otherwise, returns True."""
    resources_needed = drink['ingredients']

    for resource, amount in resources_needed.items():
        if resources[resource] < amount:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


def process_payment(drink):
    """Prompts the user for the number of each coin inserted calculating
    the total value user inserts. Then compares this value with the actual
    drink value. Display a message if the amount is not enough and returns
    False, otherwise, returns True, displaying a message if the amount is
    more than enough telling the user the change to be received."""
    price = drink['cost']

    print("Please insert coins.")
    total = 0.0
    for coin, value in coins.items():
        total += float(input(f'How many {coin}? ')) * value
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    if total > price:
        print(f"Here is ${total - price:.2f} in change.")
    return True


def change_resources(drink):
    """Change the global variables resources and money according with the
    amount used of each ingredient and the money received from the user."""
    global resources, money
    resources_needed = drink['ingredients']
    price = drink['cost']
    for resource, amount in resources_needed.items():
        resources[resource] -= amount
    money += price


def make_coffee(drink_name):
    """Checks if the resources and payment are sufficient, if they
    are display a message to the user and changes the resources"""
    drink = MENU[drink_name]
    if check_resources(drink) and process_payment(drink):
        print(f"Here is your {drink_name} ☕️. Enjoy!")
        change_resources(drink)


def coffee_machine():
    """Prompts the user for a drink name if the user types 'off'
    returns otherwise the function is recalled recursively"""
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        return
    if user_choice == 'report':
        report()
    else:
        make_coffee(user_choice)
    coffee_machine()


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    'quarters': 0.25,
    'dimes': 0.10,
    'nickles': 0.05,
    'pennies': 0.01
}
money = 0.0

coffee_machine()
