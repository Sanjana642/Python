# json file example -

import json

file_path = "C:\\Users\\Asus\\Desktop\\output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")

# output - Jasmine
