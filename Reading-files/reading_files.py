# Python Reading files (.txt, .json, .csv)

# txt file example - 

file_path = "C:\\Users\\Asus\\Desktop\\output.txt"  
# remove .txt then we will get fileNotFound error we can fix this using exception handling

# with is used to wrap the execution of a block with methods defined by context manager
# with is also used to close a file when we open it (it is best practice to close file)
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have permission to read that file")
