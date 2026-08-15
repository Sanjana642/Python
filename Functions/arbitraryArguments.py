# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments 
# (* is unpacking operator)

def add(x,y):
    return x + y

# print(add(1,2,3))  you cannot add third argument

#def add(*nums):
def add(*args):
    print(type(args))  # <class, 'tuple'>
    total = 0
    # for num in nums:
    for arg in args:
        total += arg
    return total

print(add(1,2,3))  #6

# *args = allows you to pass multiple non-key arguments
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.","Spongebob","James","III")

# **kwargs = allows you to pass multiple keyword arguments
def print_address(**kwargs):
    print(type(kwargs))  # <class, 'dict'>
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        print("-----------")

print_address(street="123 Main St", 
              city="Anytown", 
              state="CA", 
              zip="12345")


# another example of *args and **kwargs both- 
def shipping_label(*args, **kwargs):  
    #if we write first **kwargs and then *args it will give error
    print("Shipping Label:")
    for arg in args:
        print(arg, end=" ")
    print()  # Print a newline
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")

    if "apt" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('city')}, {kwargs.get('apt')}")

    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}, {kwargs.get('city')}")
        print(f"{kwargs.get('pobox')}")

    else:
        print(f"{kwargs.get('street')}, {kwargs.get('city')}")

    print(f"{kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "James", "III",
               street="123 Main St", 
               apt="Apt 4B",
               pobox="PO Box #1001"     ,
               city="Anytown", 
               state="CA", 
               zip="12345") 

# output - Shipping Label:
# Dr. Spongebob James III 
# 123 Main St, Anytown, Apt 4B
# CA 12345
#  Since "apt" exists in kwargs, the first if condition is True.
# Python executes that block and skips the elif completely.