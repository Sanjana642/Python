# if __name__ == 'main': (this script can be imported or run standalone) 
# Functions and classes in this module can be reused without 
# the main block of the code executing
# Good practice - (code is modular, helps readability,
#                  leaves no global variable, avoid unintended execution)

# library: Import library for functionality

# from script2 import * -

print(__name__)

# output - script2 __main__ (filename) 

def favourite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script 1")
    favourite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()

#output -__main__
# This is script 1
# Your favorite food is pizza
# Goodbye!