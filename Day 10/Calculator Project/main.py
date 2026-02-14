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

n1 = int(input("\nEnter first number: "))
operation = input("\nEnter + to add \nEnter - to subtract \nEnter * to multiply \nEnter / to divide \n\n:")
n2 = int(input("\nEnter second number: "))


result = operations[operation](n1, n2)
print(f"Total is {result}. ")

cont_result = input("\nWould you like to continue using the previous result? Yes|No: ")
