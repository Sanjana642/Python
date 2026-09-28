# csv writing_file example -

import json
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", "28", "Chef"],
             ["Patrick", "27", "Civil-Engineer"],
             ["John", "30", "Worker"]]

file_path = "C:\\Users\\Asus\\Desktop\\output.csv"


try:
    with open(file_path, "w", newline="") as file: 
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"Csv file '{file_path}' created successfully!")
except FileExistsError:
    print(f"Csv file '{file_path}' already exists!")

# output -
# Name,Age,Job
# Spongebob,28,Chef
# Patrick,27,Civil-Engineer
# John,30,Worker