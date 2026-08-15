# this is my first Python program
print("I like typing")
print("Its really good!")

#variable = A container for a value (string, float, integer, boolean)
# A variable behaves as if it was the value it contains

#strings
first_name = "sanjana"
email = "sanjana@gmail.com"

print(first_name)     #output - sanjana
print("first_name")   #output - first_name
print (f"Hello {first_name}")  #this will print Hello sanjana
print (f"My email is {email}")   #my email is sanjana@gmail.com


#integers
age = 24
quantity = 2
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"You have {num_of_students} students")

#float
price = 5.99
distance = 4.4

print(f"The price is {price} dollars.")
print(f"The distance is {distance} meters.")


#boolean
is_student = True
for_sale = True

if is_student:
    print("You are a student.")
else:
    print("You are not a student.")

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not available.")

#Typecasting = the process of converting a variable from one data to another str(), int(), float(), bool()

# name = "sanjana"
age = 24
gpa = 3.2
is_student = True

print(type(age))
#output - <class 'int'>

print(type(gpa))
#output - <class 'float'>

#this will convert to int 3.2 = 3
gpa = int (gpa)
print (gpa)

#this will convert to boolean - true
is_student = bool (is_student)
print(is_student)

#this will remain int only if we declare the type str -
age = str(age)
age += 1
#output = error - cannot concatenate str to int to str

# if age += "1" then output will be 251

print(age)
#output - 25 though it is string
print(type(age))
#output - <class 'string'>

#input = A function that prompts the user to enter data. Returns the entered data as a string

name = input("What is your name? ")
age = int(input("How old are you? "))

age = age +1
print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"Your age is {age}.")
