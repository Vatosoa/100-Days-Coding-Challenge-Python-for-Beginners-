file_path = '/home/vatosoa/vs_code/projet/Python/100 days challenge of code/100 days of coding challenge for beginners/VII. File Handling/sample.txt'

data = "\nThis is additional data"

with open(file_path, 'a') as file:
    file.write(data)
    