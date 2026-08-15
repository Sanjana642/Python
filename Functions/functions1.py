#Functions = A block of reusable code place () after the function name to invoke it

# if we want to repeat this song for 3 times -
def happy_birthday(name):
    print(f"Happy Birthday to {name}...")
    print("Happy Birthday to you")
    print("May god bless you")
    print("Happy Birthday to you!!!")
    print()

happy_birthday("Broo")
happy_birthday("Steve")
happy_birthday("Joe")


# if we want to pass name and age (arguments and parameters position should same) -
def happy_birthday(name, age):  
    print(f"Happy Birthday to {name}...")
    print("Happy Birthday to you")
    print(f"You are {age} years old")
    print("Happy Birthday to you!!!")
    print()

happy_birthday("Broo",22)
happy_birthday("Steve",21)
happy_birthday("Joe",22)
