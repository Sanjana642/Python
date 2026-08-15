# if - Do some code only IF conditon is true -Else do something else

# if with integer value --
age = int(input("Enter your age :"))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
elif age >=100 :
    print("You are too old to sign ip")
else :
    print("You must be 18+ to sign up.")


# if with input value --
response = input("Would you like to have some food? (Y/N) :")

if response == "Y":
    print("Yes, we would like to have some food.")
else : 
    print("Ok, no worries.")


# if with empty string --
name = input("enter your name: ")

if name == " ":
    print("You have not entered your name!")
else :
    print(f"Hello {name}")


# if with boolean value --
for_sale = True

if for_sale:
    print("This item is for sale.")
else :
    print("This item is NOT for sale")

# if with boolean value --
online = False

if online:
    print("The user is online")
else :
    print("The user is offline")