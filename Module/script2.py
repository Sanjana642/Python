# from script2 import * - 
print(__name__)
# output - script1 (filename) __name__ 

from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

# print("This is script 2")
# favourite_food("pasta")
# favourite_drink("matcha")
# print("Thankyou!")

def main():
    print("This is script 2")
    favourite_food("pasta")
    favourite_drink("matcha")
    print("Thankyou!")

if __name__ == "__main__":
    main()

# this main can run standalone program