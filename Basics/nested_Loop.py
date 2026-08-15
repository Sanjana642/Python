# nested loop = a loop within another loop (outer, inner)
# outer loop:
#     inner loop:

# eg - while-while loop, for-for loop, while-for loop, for-while loop, etc

for x in range(1, 10):
    print(x, end = " ")
#output - 1 2 3 4 5 6 7 8 9

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
#output - 123456789
# 123456789
# 123456789