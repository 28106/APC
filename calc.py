import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def factorial(a):
    if a < 0:
        return "Error: Factorial of a negative number is not defined."
    return math.factorial(a)

def calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Cube")
    print("7. Factorial")
    
    choice = input("Enter choice (1-7): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print("Result:", addition(num1, num2))
        elif choice == '2':
            print("Result:", subtraction(num1, num2))
        elif choice == '3':
            print("Result:", multiplication(num1, num2))
        elif choice == '4':
            print("Result:", division(num1, num2))
    
    elif choice in ['5', '6', '7']:
        num = int(input("Enter a number: "))
        
        if choice == '5':
            print("Result:", square(num))
        elif choice == '6':
            print("Result:", cube(num))
        elif choice == '7':
            print("Result:", factorial(num))
    
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()