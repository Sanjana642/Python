#concession stand program

menu = {
    "pizza" : 7.00,
    "nachos" : 4.45,
    "popcorn" : 1.45,
    "fries" : 3.45,
    "penne pasta": 12.56,
    "chips" : 2.05,
    "burger" : 5.80,
    "sandwich" : 5.78,
    "pretzel" : 8.02
}   

cart = []
total = 0

print("------ MENU ------")
for key,value in menu.items():
    print(f"{key} : ${value}")
print("-----------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
# print(cart)

print("----YOUR CART----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")