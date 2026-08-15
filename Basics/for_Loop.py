#for loop = execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc

for x in range (1,11):
    print(x)  # you can name x = counter

#output - 1 to 10 numbers

for counter in reversed(range (1,11)):
    print(counter)  # you can name x = counter

print("Happy New Year!")
#output - reversed 1 to 10 numbers then Happy New Year!

for x in range (1,11,2):
    print(x)
#output - 1 3 5 7 9

credit_card = 1234-5678-9012

for x in credit_card:
    print(x)
#output - 1234-5678-9012 


for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)
# output - 1 to 20 numbers except 13 (condition)

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x)
# output - 1 to 12 numbers due to break (condition)

