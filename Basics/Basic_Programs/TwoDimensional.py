#1 program -Two dimensional list program

fruits = ["apple", "strawberry", "pineapple", "guava", "banana"]
vegetables = ["celery","carrots","potatoes"]
meats = ["chicken","fish","turkey"]

groceries = [fruits,vegetables,meats]

print(groceries)  #all arrays will print inside one array

print(groceries[0])  #at index 0 fruits list will show at 1-vegetables and 2-meats

print(groceries[0][0])  #apple will print
print(groceries[1][0])  #celery will print
print(groceries[2][2])  #turkey will print
# print(groceries[0][5])  #error - list index out of range

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


#2 program - Two Dimensional Keypad

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

