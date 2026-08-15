#Logical Operators = evaluate multiple conditions(and, or, not)
# and = both conditions must be True
# or = atleast one condition must be True
# not = inverts the condition (not False, not True)

# 1. Or Example - 
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining: 
    print("The outdoor event is cancelled")
else :
    print("The outdoor event is still scheduled")

# if temp is higher than 35 then it will print else statement 


# 2. And Example - 
temp = 25
is_sunny = True 

# when temp is 33 this will execute-
if temp >= 28 and is_sunny :
    print("It's HOT outside!")
    print("It is sunny!")

# when temp is -5 this will execute-
elif temp <= 0 and is_sunny :
    print("It's COLD outside!")
    print("It is sunny!")

# when temp is 20 this will execute-
elif 28 > temp > 0 and is_sunny :
    print("It's WARM outside!")
    print("It is sunny!")


# 3. Not Example -
if temp >= 28 and is_sunny :
    print("It's HOT outside!")
    print("It is sunny!")

elif temp <= 0 and is_sunny :
    print("It's COLD outside!")
    print("It is sunny!")

elif 28 > temp > 0 and is_sunny :
    print("It's WARM outside!")
    print("It is sunny!")

# when temp is 28 this will execute-
elif temp >= 28 and not is_sunny :
    print("It's HOT outside!")
    print("It is CLOUDY!")

# when temp is 0 this will execute-
elif temp <= 0 and not is_sunny :
    print("It's COLD outside!")
    print("It is CLOUDY!")

# when temp is 20 this will execute-
elif 28 > temp > 0 and not is_sunny :
    print("It's WARM outside!")
    print("It is CLOUDY!")