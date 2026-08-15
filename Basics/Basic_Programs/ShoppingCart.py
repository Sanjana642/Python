#Shopping cart program -

item = input ("what item do you like to buy? : ")
price = float(input("Enter the price of the item: "))
quantity = int(input("How many would you like? : "))
total = price * quantity

print(total)

print(f"You have bought {quantity} x {item}/s")
print(f"your total is {total}")