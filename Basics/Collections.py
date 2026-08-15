#collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. No duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. Faster (than list)

# 1. List = []
fruits = ["apple", "banana", "guava", "strawberry"]

print(fruits[1])
print(fruits[::2]) #['apple','guava']
print(fruits[::-1]) #reverse order

for fruit in fruits:
    print(fruit)  
    print(dir(fruits)) #it will show all methods which you can use
    print(help(fruits)) #it will give detail description of methods 
    print(len(fruits)) #4 
    print("apple" in fruits) #True

#output - every fruit in order

fruits.append("pineapple") # this fruit will appear last 
fruits.remove("apple")  #it will remove apple
fruits.insert(0, "mulberry")  #it will add mulberry at first position
fruits.sort() #sort according to ascending order
fruits.reverse() #all fruits will display reverse order
fruits.clear()  #it will clear all fruits - []
fruits.index("apple")  #output will be 0 if not found = error (pineapple is not list)
fruits.count("apple")  #will return 1 if found else 0 when not found

fruits[0] = "pineapple"  #duplicates are Ok

for fruit in fruits:
    print(fruits)
# output - pineapple banana guava strawberry


# 2. Set = {}
colors = {"green", "black", "crimson", "white"}
# all above methods of list 

# if we duplicate value in set it will still return one value only-
colors = {"green", "black", "crimson", "white", "black"}
#output - {"green", "black", "crimson", "white"}

# 3. Tuple = ()
fruits = ("apple", "banana", "guava", "strawberry", "guava")
fruits.count("guava") #2 duplicates are OK
