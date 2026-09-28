# python writing files (.txt, .json, .csv)

# txt file example -

txt_data = 'I Like Pizza!'

file_path = "C:\\Users\\Asus\\Desktop\\output.txt"

# w = write mode, x = also write mode when doesn't exists, a = append file, r = read file
try:
    # with open(file_path, "w") as file:
    with open(file_path, "a") as file:  
        # w indicates write mode, if the file already exists, it will be overwritten
        # x indicates exclusive creation,(fileExistsError) -
        # if the file already exists, the operation will fail 
        # a is used to append old data with new data

        # file.write(txt_data)
        file.write("\n" + txt_data)
        print(f"Text file '{file_path}' created successfully!")
except FileExistsError:
    print(f"Text file '{file_path}' already exists!")

# output -
# a = I Like Pizza!
# I Like Pizza! - 2 times with new line