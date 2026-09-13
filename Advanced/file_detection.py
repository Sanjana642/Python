# Python file detection = 

import os 

file_path = "C:\\Users\\Asus\\Desktop\\test.txt"  
# if filepath is basic/test.txt or any C:\Users\HP - 
# it gives warning because \t = tab so-
# we either need to use / slash or \\ (C:\\Users\\HP)

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("This location doesn't exists")
# output - The location 'test.txt' exists
