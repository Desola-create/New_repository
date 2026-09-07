def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
def loop():
    while True:

        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == '+':
            result = add(num1, num2)
            print("The result is: ", result)
        elif operator == '-':
            result = minus(num1 , num2)
            print("The result is: ", result)
        elif operator == '*':
            result = multiply (num1 , num2)
            print("The result is: ", result)
        elif operator == '/':
            result = divide (num1,num2)
            print("The result is: ", result)
        else:
            print("Invalid operator. Please use +, -, *, or /.")

loop()        