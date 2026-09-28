# continued here-
# txt file example-

employees = ["Squidward", "Patrick", "Spongebob", "John"]

file_path = "C:\\Users\\Asus\\Desktop\\output.txt"

try:
    with open(file_path, "w") as file: 
        for employee in employees: 
            file.write(employee + "\n")
            print(f"Text file '{file_path}' created successfully!")
except FileExistsError:
    print(f"Text file '{file_path}' already exists!")

# output = 
# if w = TypeError: write() argument must be str, not list