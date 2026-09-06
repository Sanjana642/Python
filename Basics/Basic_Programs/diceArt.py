# dice art program -
import random

# print("\u25cF \u250c \u2500 \u2510 \u2502 \u2502 \u2514 \u2500 \u2518") for asci art 

dice_art ={
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    )
}

dice = []
total = 0
num_of_dice = int(input("How many dice do you want to roll? "))

for die in range(num_of_dice):    
    dice.append(random.randint(1, 6))

# for die in range(num_of_dice):    
#     print(f"Die {die + 1}:")
#     for line in dice_art[dice[die]]:
#         print(line)   
#     print()

#to print dice horizontally (line 1 to 5 tuple from all dice numbers)
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()  #identation

for die in dice:
    total += die

print(f"Total: {total}")
