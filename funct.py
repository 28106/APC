def greet():
    print("Hello, Welcome to Python!")


greet()



def add(a, b):
    return a + b

print(add(5, 10))  


def greet(name="Guest"):
    print("Hello,", name)

greet("Swapnali")   
greet()             


def student(name, age):
    print(f"Name: {name}, Age: {age}")

student(age=21, name="Riya")  


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))   


