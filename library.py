class Book:
    def __init__(self, title, author):
        self.__title = title          
        self.__author = author
        self.__is_issued = False

    def issue(self):
        if not self.__is_issued:
            self.__is_issued = True
            return True
        return False

    def return_book(self):
        if self.__is_issued:
            self.__is_issued = False
            return True
        return False

    def is_available(self):
        return not self.__is_issued

    @property
    def title(self):   
        return self.__title

    def __str__(self):
        status = "Available" if self.is_available() else "Issued"
        return f"{self.__title} by {self.__author} - {status}"


class Member:
    def __init__(self, name, borrow_limit):
        self.name = name 
        self.borrow_limit = borrow_limit
        self.borrowed_books = []

    def borrow(self, book: Book):
        if len(self.borrowed_books) < self.borrow_limit and book.issue():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"{self.name} cannot borrow '{book.title}'")

    def return_book(self, book: Book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")


class StudentMember(Member):  
    def __init__(self, name):
        super().__init__(name, borrow_limit=2)


class FacultyMember(Member):  
    def __init__(self, name):
        super().__init__(name, borrow_limit=5)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)



lib = Library()
b1 = Book("Python Basics", "John Doe")
b2 = Book("Data Science", "Alice Smith")
lib.add_book(b1)
lib.add_book(b2)

s1 = StudentMember("Ravi")
f1 = FacultyMember("Dr. Sharma")

s1.borrow(b1)     
f1.borrow(b1)       
f1.borrow(b2)      
s1.return_book(b1)
lib.show_books()
