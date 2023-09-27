import os

file_path = '/home/vatosoa/vs_code/projet/Python/100 days challenge of code/100 days of coding challenge for beginners/VII. File Handling/test.txt'

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted successfully")
else:
    print(f"{file_path} does not exist")