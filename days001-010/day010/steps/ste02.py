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

num1 = int(input("What's the first number? "))

print("  ".join(operations))
operation_symbol = input("Pick an operation from the line above: ")

num2 = int(input("What's the second number? "))

calculation_function1 = operations[operation_symbol]
answer1 = calculation_function1(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer1}")

operation_symbol = input("\nPick another operation: ")

num3 = int(input("What's the next number? "))

calculation_function2 = operations[operation_symbol]
answer2 = calculation_function2(calculation_function1(num1, num2), num3)

print(f'{answer1 } {operation_symbol} {num3} = {answer2}')
