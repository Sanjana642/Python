# conditonal expressions = A one-line shortcut for the if-else statement(ternary operator)
# Print or assign one or two values based on condition
# X if condition else Y

num = 5

print("Positive" if num > 0 else "Negative")
#output - positive

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)
#output - ODD

a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b

print(max_num) 
#output - 7

print(min_num)
#output - 6

age = 25
status = "Adult" if age >= 18 else "Child"
print(status)
#output - Adult

temperature = 20
weather = "HOT" if temperature > 20 else "COLD"
print(weather)
#output - COLD

user_role = "admin"
access = "Full access" if user_role == "admin" else "Limited access"
print(access)
#output - Full access
