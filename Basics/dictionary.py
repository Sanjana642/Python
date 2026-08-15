#dictionary = a collection of {key: value} pairs. It is ordered and changeable. NO duplicates

capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(dir(capitals))
# print(help(capitals))

print(capitals.get("India"))  #if (Japan) none will return

if capitals.get("japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany" : "Berlin"})
capitals.pop("USA")
capitals.popitem() #it will remove the last element

keys = capitals.keys()
print(keys)  #all keys will print

print(capitals)

keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

#items = capitals.items()
for key,value in capitals.items():
    print(f"{key}:{value}")