def add (a, b):
    sum = a + b
    return sum

def subtract (a, b):
    diff = (a - b)
    return diff

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

def calculate():
    operation = input("Enter operation (+, -, *, /): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "+":
        result = add(a, b)
    elif operation == "-":
        result = subtract(a, b)
    elif operation == "*":
        result = multiply(a, b)
    elif operation == "/":
        result = divide(a, b)
    else:
        result = "Invalid operation"

    print(f"The result is: {result}")

calculate()