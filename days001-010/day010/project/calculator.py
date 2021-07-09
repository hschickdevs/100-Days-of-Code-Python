import os

import art


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number? "))

    print("  ".join(operations))

    keep_calculating = 'c'
    while keep_calculating == 'c':
        operation_symbol = input("Pick an operation: ").strip()

        num2 = float(input("What's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        num1 = answer

        keep_calculating = input(
            f"Type 'c' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower()

        if keep_calculating == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            calculator()


calculator()
