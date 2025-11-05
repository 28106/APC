class Person:
    name = "Swapnali"
    occupation = "Student"
    roll_no = 106

    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()
b = Person()
a.name = "xyz"
a.occupation = "Accountant"

b.name = "abc"
b.occupation="HR"
# print(a.name)
# print(a.occupation)
# print(a.roll_no)
a.info()
b.info()