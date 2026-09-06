#Shopping cart Program

foods = []
prices = []

total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
    
print("---- YOUR CART ----")

for food in foods:
    # print(food, end=" ") to add list items horizontally
    print(food)  #to add items vertically

for price in prices:
    total += price

print()  # for new line
print(f"Your total is: {total}")