import os

directory_path = '/home/vatosoa/vs_code/projet/Python/100 days challenge of code/100 days of coding challenge for beginners/VII. File Handling/text'

if os.path.exists(directory_path):
    print(f"{directory_path} exists")
else:
    print(f"{directory_path} does not exists")