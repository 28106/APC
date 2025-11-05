from abc import ABC, abstractmethod

class Movie(ABC):
    def type(self):
        pass

class Horror(Movie):
    def type(self):
        return "This is horror movie!"
    

class Comedy(Movie):
    def type(self):
        return "This is Comedy Movie!"


class Biopic(Movie):
    def type(self):
        return "This is Biopic Movie!"
    

class Thriller(Movie):
    def type(self):
        return "This is Thriller Movie!"
    
class SciFic(Movie):
    def type(self):
        return "This is Science Fiction Movie!"
    

class Action(Movie):
    def type(self):
        return "This is Action Movie!"
    
class Drama(Movie):
    def type(self):
        return "This is Draman Movie!"

class Adventure(Movie):
    def type(self):
        return "This is Adventure Movie!"
    
class Fantasy(Movie):
    def type(self):
        return "This is Fantasy Movie!"

class Documentary(Movie):
    def type(self):
        return "This is Documentary Movie!"
    
class Mystery(Movie):
    def type(self):
        return "This is Mysterious Movie!"
    
h = Horror()
c = Comedy()
b = Biopic()
t = Thriller()
s = SciFic()
a = Action()
d = Drama()
ad = Adventure()
f = Fantasy()
do = Documentary()
m = Mystery()

print(h.type())
print(c.type())
print(b.type())
print(t.type())
print(s.type())
print(a.type())
print(d.type())
print(ad.type())
print(f.type())
print(do.type())
print(m.type())


genres = {
    "1": Horror(),
    "2": Comedy(),
    "3": Biopic(),
    "4": Thriller(),
    "5": SciFic(),
    "6": Action(),
    "7": Drama(),
    "8": Adventure(),
    "9": Fantasy(),
    "10": Documentary(),
    "11": Mystery()
}

while True:
    print("\n--- Movie Genre Menu ---")
    print("1. Horror")
    print("2. Comedy")
    print("3. Biopic")
    print("4. Thriller")
    print("5. Science Fiction")
    print("6. Action")
    print("7. Drama")
    print("8. Adventure")
    print("9. Fantasy")
    print("10. Documentary")
    print("11. Mystery")
    print("0. Exit")

    

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Thank you! Exiting...")
        break

    movie = genres.get(choice)
    if movie:
        print(movie.type())
    else:
        print("Invalid choice! Please try again.")
