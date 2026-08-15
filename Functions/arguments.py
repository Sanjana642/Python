# default arguments = A default value for certain parameters, 
#                     default is used when that argument is omitted
#                     make your functions more flexible,reduces # of arguments
#  1. positional  2. default  3. keyword  4. arbitrary 
# (last example of functions positional arguments were discussed)
 

# 2. default arguments example-
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))  # 525.0 output
print(net_price(500, 0.1)) # 472.5
print(net_price(500, 0.1, 0)) # 450.0

# another example-

import time

# def count(start, end):
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

# count(0,10)
count(10)
count(30,15) #starts from 15 end with 30

# 3. keyword arguments = an argument preceded by a identifier helps with readability
#                        order of arguments doesnt matter

# keyword arguments example-

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hellooo","Mrs.","Smita","Desai")
hello("Hello", title="Mr.", last="John", first="James") #to understand the arguments

# another example -
for x in range(1,11):
    print(x, end=" ")

print("1","2","3","4","5", sep="-") #1-2-3-4-5

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=677, last=8001)
print(phone_num)

# arbitrary arguments in next file