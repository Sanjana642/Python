# String Methods -

name = input("enter your full name: ")

#1 result = len(name)
#2 result = name.find(" ")
#3 result = name.find("B")
#4 result = name.find("o")  first o
#5 result = name.rfind("o")  last o (r means reverse)
#6 result = name.rfind("q")  (will return negative)
#7 name = name.capitalize()
#8 name = name.upper()
#9 name = name.lower()
#10 result = name.isdigit()
#11 result = name.isalpha() (no space should there else false wil return)

print(result)
print(name)
#1 output - Bro Code = 8
#2 output - Bro Code = 3
#3 output - Bro Code = 0
#4 output - Bro Code = 2 (position)
#5 output - Bro Code = 5 (position)
#6 output - Bro Code = -1 (no q present)
#7 output - name - bro code = Bro code (only first letter will be capital)
#8 output - Bro code = BRO CODE (upper method)
#9 outpupt - BRO CODE = bro code (lower)
#10 output - bro123 = False (false if only digits are contain) 123 = true
#11 output - Bro Code - false (due to space)  brocode - true

phone_number = input("Enter your phone number #: ")
# result = phone_number.count("-")
# result = phone_number.replace("-", " ")
print(result)
#output - 1-232-453-674-788  = 4 (to count the characters)
#output - 1 232 453 674 788 (replaced with space)

