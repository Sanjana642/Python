#format_specifiers = {value:flags} format a value based on what flags are interested

# .(number)f = round to that many decimal places(fixed_point)
# :(number) = allocate to many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3.14159
price2 = -977.89
price3 = 12.34

print(f"Price 1 is ${price1: .2f}")
print(f"Price 2 is ${price2: .2f}")
print(f"Price 3 is ${price3: .2f}")

#output -
# Price 1 is $3.14
# Price 1 is $-977.89
# Price 1 is $12.34

print(f"Price 1 is ${price1:10}") #1
print(f"Price 1 is ${price1:010}") #2
print(f"Price 1 is ${price1:<10}")
print(f"Price 1 is ${price1:>10}")
print(f"Price 1 is ${price1:^10}")
print(f"Price 1 is ${price1:+}")
print(f"Price 1 is ${price1: }")  #negative num will have no space
print(f"Price 1 is ${price1:,}")  #price1 = 3000.14159
print(f"Price 1 is ${price1:,.2f}")  #price1 = 3000.14159

#1 Price 1 is $    3.14 - with 10 spaces
#2 Price 1 is $0003.14
#3 Price 1 is $3.14159
#4 Price 1 is $    3.14159 
#5 Price 1 is $ 3.14159
#6 Price 1 is $+3.14159
#7 Price 1 is $ 3.14159
#8 Price 1 is $3.14159
#9 Price 1 is $ 3.14
