import random

low = 1
high = 100
options = ("rock","paper","scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# print(help(random))
# number = random.randint(1, 20)
# number = random.random()
# option = random.choice(options)  #choice will choose any random option
random.shuffle(cards)  #use for shuffling cards

# print(number)
# print(option)
print(cards)  