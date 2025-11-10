# class Car:
#     def __init__(self):
#         self.make = "Toyota"
#         self.model = "Corolla"
#         self.year = 2022
# c = Car();
# print(c.make)
# print(c.model)
# print(c.year)


class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        print("Constructor called: Car object created")

    # Destructor
    def __del__(self):
        print("Destructor called: Car object destroyed")


c = Car("Honda", "Civic", 2022)


print("Make:", c.make)
print("Model:", c.model)
print("Year:", c.year)


del c

# print("Program end")



class UserInput:
    def __init__(self):
        self.name = input("Enter your name:")
        self.age = int(input("Enter your age:"))

        print(f"Constructor called: Hello: {self.name}, age: {self.age}")

    def __del__(self):
        print(f"Destructor called")

u = UserInput();
del u
