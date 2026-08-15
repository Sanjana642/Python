# List Comprehension = A concise way to create list in python.
#                       Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)
print(doubles)
# output -[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# [expression for value in iterable if condition]
doubles = [x * 2 for x in range(1,11)]
triples = [y * 3 for y in range(1,11)]
squares = [z * z for z in range(1,11)]
print(doubles)
print(triples)
print(squares)
# output -[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# output -[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# output- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# String example-

fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
#fruits = [fruit.upper() for fruit in ["apple","orange","banana","coconut"]] 
# - you can write in one line
print(fruits)
# output -['APPLE', 'ORANGE', 'BANANA', 'COCONUT']

numbers = [1, -2, 3, -4, -5, 6, -7, 8, 9]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0] 
odd_nums = [num for num in numbers if num % 2 == 1] 

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
#output = [1, 3, 6]
#output = [-2, -4, -5]
#output = [-2, -4, 6]
#output = [1, 3, -5]

grades = [86, 45 ,89, 34, 65, 22, 93, 77]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
