# decorator = A function that takes another function as an argument and extends its behavior without explicitly modifying it. 
# Decorators are often used to add functionality to existing functions or methods, such as logging, authentication, or caching.
# Pass the base function as an argument to the decorator function and return a new function that adds the desired functionality.
# eg- @add_sprinkles 
#      get_ice_cream("vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You have added with sprinkles on top! 🍬")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge 🍫")
        func(*args, **kwargs) 
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream! 🍨")

get_ice_cream("pista")  
# Output: You have added with sprinkles on top! 🍬
# You add fudge 🍫
# Here's your pista ice cream! 🍨

# wrapper is called a closure function because it is defined inside another function and has access to the variables of the outer function.
# when we call get_ice_cream(), it actually calls the wrapper() function, which adds the sprinkles and then calls the original get_ice_cream() function.
