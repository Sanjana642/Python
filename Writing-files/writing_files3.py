# json file example - 

import json

employee = {
    "name": "Jasmine",
    "age": "26",
    "job": "care-taker"
}

file_path = "C:\\Users\\Asus\\Desktop\\output.json"


try:
    with open(file_path, "w") as file: 
        json.dump(employee, file, indent=4)   
        # dump method will convert dict to json string to import it
        print(f"Json file '{file_path}' created successfully!")
except FileExistsError:
    print(f"Json file '{file_path}' already exists!")

# output-
# {"name": "Jasmine", "age": "26", "job": "care-taker"} 

# indent=4 (with spaces of 4)- {
    # "name": "Jasmine",
    # "age": "26",
    # "job": "care-taker"
# }