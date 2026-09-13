# car_variables = Shared among all instances of a class
#                 Defined outside the constructor
#                 Allow you to share data among all objects created from that class

class Car:
    wheels = 4  # class variables
    
    def __init__(self, model, year):
        self.model = model       # instance variables
        self.year = year

# example-
class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob",30)
student2 = Student("Patrick",29)
student3 = Student("Squidward", 28)

print(student1.name)
print(student1.age)
print(Student.class_year)  
# output - Spongebob 30 2025

print(student2.name)
print(student2.age)
print(Student.class_year)
# output - Patrick 29 2025

# its better to add classname Student instead of 
# object created from that class such as student1

print(Student.num_students)  
# output - 2

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)

# output-  My graduating class of 2025 has 3 students. (with names of students)