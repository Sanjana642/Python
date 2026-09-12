# static methods =  a method that belongs to class rather than any object from that class(instance) usually need for generally utility functions 

# Instance Methods - best for operations of instances of the class (objects)
# Static Methods - best for utility functions that do not need access to class data


# Static method example -
class Employee:

    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "HR", "Developer", "Sales"]
        return position in valid_positions

employee1 = Employee("Eugene","Manager")
employee2 = Employee("Squidward","HR")
employee3 = Employee("Spongebob", "Developer")

print(Employee.is_valid_position("HR"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
