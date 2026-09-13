# object = A "bundle" of related attributes (variables) and methods (functions)
# Ex. phone, book, cup 
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of the object

from car import Car

car1 = Car("Porsche", 2024, "black", False)
car2 = Car("Ferrari", 2025, "orange", False)
car3 = Car("Corvette", 2026, "blue", True)

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)

car1.drive()
car2.drive()
car3.drive()

car1.describe()
