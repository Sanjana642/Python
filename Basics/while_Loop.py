#while loop = execute some code while some condition remains TRUE

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!") #only this stmt will run continuous
    print("Enter your name: ")

print(f"Hello {name}")
#output - You did not enter your name  (Runs the condition until its true)
#Enter your name:
# You did not enter your name
#Enter your name: bro
# Hello bro

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")
#output - enter your age: 21


food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit): ")

print("bye")
#output - Enter a food you like (q to quit): ramen
# You like ramen
# Enter a food you like (q to quit): q
# bye


num = int(input("Enter a # between 1 to 10: "))

while num < 1 or num > 10:
    print("{num} is not valid")
    num = int(input("Enter a # between 1 to 10: "))

print(f"Your number is {num}")