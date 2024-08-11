import os

# Specify the directory you want to list
directory_path = '/'

# List all files and directory in the Specified path
contents = os.listdir(directory_path)

# Print each file and directory name
for item in contents:
    print(item)
