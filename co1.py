# class Student:
#     student_name = "Tony Stark"
#     marks = 93

# print(f"Student Name: {getattr(Student,'student_name')}")
# print(f"Student Marks: {getattr(Student,'marks')}")

# setattr(Student, 'student_name', 'Peter Parker')
# setattr(Student, 'marks', '95')

# print(f"After Modifying, Student Name:{getattr(Student, 'student_name')}")
# print(f"Student Marks:{getattr(Student, 'marks')}")



# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
    
# s1 = Student("Ravi", 20, "Computer Science")

# print("Before modification:", s1.__dict__)

# s1.age = 21
# s1.course = "Data Science"

# print("After Modification:", s1.__dict__)


# class Rectangle:
#     def __init__(self, l, w):
#         self.lenghth = l
#         self.width = w

#     def area(self):
#         return self.lenghth*self.width
# r = Rectangle(5, 10)
# print("area of rectangle is:",r.area())


# class StringHandler:
#     def __init__(self):
#         self.text = ""

#     def get_String(self):
#         self.text = input("Enter a string: ")

#     def print_String(self):
#         print(self.text[::-1].upper())

# s = StringHandler()
# s.get_String()
# s.print_String()



class stringop:
    def __init__(self):
        self.text = ""

    def get_sting(self):
        self.text = input("Enter a string:")

    

    def get_lower(self):
        print(f"Lower String is:",self.text.lower())

    def get_upper(self):
        print(f"Uppercase string is:",self.text.upper())

p = stringop()
p.get_sting()
p.get_lower()
p.get_upper()


