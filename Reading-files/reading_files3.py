# csv file example -

import csv

file_path = "C:\\Users\\Asus\\Desktop\\output.csv"

try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")

# output - Name,Age,Job
# Spongebob,28,Chef
# Patrick,27,Civil-Engineer
# John,30,Worker

# output when added for loop-
# ['Name', 'Age', 'Job']
# ['Spongebob', '28', 'Chef']
# ['Patrick', '27', 'Civil-Engineer']
# ['John', '30', 'Worker']

# output - line[0] will return first column
# Name
# Spongebob
# Patrick
# John

