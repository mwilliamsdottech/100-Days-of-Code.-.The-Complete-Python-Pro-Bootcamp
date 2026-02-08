def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

n1 = input("\nEnter first number: ")
operation = input("\nEnter + to add \nEnter - to subtract \nEnter * to multiply \nEnter / to divide \n\n:")
n2 = input("\nEnter second number: ")

if operation