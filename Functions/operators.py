# Membership operators are used to test if a sequence is presented in an object.
# (string, list, tuple, set, dictionary etc.)
# 1. in - Returns True if a sequence with the specified value is present in the object
# 2. not in - Returns True if a sequence with the specified value is not present

word = "APPLE"

letter = input("Guess a letter in a secret word: ")

if letter in word:
    print(f"Good guess! {letter} is in the word.")
else:
    print(f"{letter} is not in the word.")
    print("------")
# in - checks if the letter is present in the word and returns True or False.

if letter not in word:
    print(f"{letter} is in the word.")
else:
    print(f"Good guess! {letter} is not in the word.")
# not in - checks if the letter is not present in the word and returns True or False.


# Example 1 -

students = ["John", "Bro", "Alice", "Bob"]

student_name = input("Enter a student name: ")

if student_name in students:
    print(f"{student_name} is a student.")
else:
    print(f"{student_name} is not a student.")
# output - Alice is a student.

if student_name not in students:
    print(f"{student_name} is not a student.")
else:
    print(f"{student_name} is a student.")
# output - Bob is a student.


# Example 2 -
grades = {"John": "A", "Bro": "B", "Alice": "C", "Bob": "D"}

student_name = input("Enter a student name: ")

if student_name in grades:
    print(f"{student_name} grade is {grades[student_name]}.")  
else:
    print(f"{student_name} is not a student.")


# Example 3 -

email = "john@example.com"

if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")
# output - Valid email address.
