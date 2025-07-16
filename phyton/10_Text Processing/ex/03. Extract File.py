file_path = input()
file_path_list = file_path.split("\\")
file_name, file_extension = file_path_list[-1].split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
