class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c=0):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20))
print (obj.add(10,20,30))


#Using default argument
class Greet:
   def hello(self, name = "Guest"):
      print(f"Hello, {name}!")
g = Greet()
g.hello()
g.hello("Amit")



#Using Variable Arguments(*args)
class Calculator:
   def multiply(self, *args):
      result = 1
      for num in args:
         result *= num
      print("Product is:", result)
c = Calculator()
c.multiply(2, 3)
c.multiply(2, 3, 4)


# #Using Keyword Argument
class Student:
   def details(self, **kwargs):
      for key, value in kwargs.items():
         print(f"{key}: {value}")
s = Student()
s.details(age=20, add="Kop", name="swap", id=106)


# #Polymorphism(Overriding)
class Animal:
   def sound(self):
      return "Some generic sound"
class Dog(Animal):
   def sound(self):
      return "Bark"
class Cat(Animal):
   def sound(self):
      return "Meow"
a = [Dog(), Cat(), Animal()]
for i in a:
   print(i.sound()) 


class Vehicle:
   def type(self, *args):
      if len(args) == 1:
         print(f"Vehicle Type: {args[0]}")
      elif len(args) == 2:
         print(f"Vehicle Type: {args[0]}, Brand: {args[1]}")
      elif len(args) == 3:
         print(f"Vehicle Type: {args[0]}, Brand:{args[1]}, Model:{args[2]}")
      else:
         print("Invalid number of details!")
v = Vehicle()
v.type("Car")
v.type("Bike", "Hero")
v.type("Truck", "Tata","2024")


