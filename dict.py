
d1 = {}


d2 = {"name": "Swapnali", "age": 21, "city": "Pune"}


d3 = dict(id=101, course="Python", duration="3 months")

print(d2)


student = {"name": "Swapnali", "marks": 95, "city": "Pune"}

print(student["name"])      
print(student.get("marks"))  
print(student.get("gender", "Not Found"))  



student = {"name": "Swapnali", "marks": 95}
student["city"] = "Pune"       
student["marks"] = 98          

print(student) 




student = {"name": "Swapnali", "age": 21, "city": "Pune"}

student.pop("age")     
print(student)

student.popitem()       
print(student)

del student["city"]    
print(student)

student.clear()       
print(student)


person = {"name": "Swapnali", "age": 21}

print(person.keys())     
print(person.values())   
print(person.items())    


extra = {"city": "Pune"}
person.update(extra)
print(person)  


students = {
    "101": {"name": "Swapnali", "marks": 95},
    "102": {"name": "Riya", "marks": 89}
}

print(students["101"]["name"]) 

