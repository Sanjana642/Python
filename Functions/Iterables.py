# Iterables = An object/collection of objects that can return its elements one at a 
# time, allowing it to be iterated over in a for-loop.

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)   # 1 2 3 4 5

for num in reversed(numbers):
    print(num, end=" ")  # 5 4 3 2 1

numbers = (1, 2, 3, 4, 5)
# same output as above

#another example of iterables -
fruits={"apple", "banana", "orange"}

for fruit in fruits:
    print(fruit)  # apple banana orange

for fruit in reversed(fruits):
    print(fruit, end=" ")  # error - TypeError: 'set' object is not reversible
 # if we assign values to a list then it will work fine in a set

name = "Bro Code"

for character in name:
    print(character, end=" ")  # B r o   C o d e

my_dict = {"name": "Bro", "age": 5, "city": "New York"}

for key in my_dict:
    print(key)  # name age city

for value in my_dict.values():
    print(value)  # Bro 5 New York

for key, value in my_dict.items():
    print(key, value)  # name Bro age 5 city New York