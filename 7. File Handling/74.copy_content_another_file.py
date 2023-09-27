source_file = '/home/vatosoa/vs_code/projet/Python/100 days challenge of code/100 days of coding challenge for beginners/VII. File Handling/sample.txt'
destination_file = '/home/vatosoa/vs_code/projet/Python/100 days challenge of code/100 days of coding challenge for beginners/VII. File Handling/test.txt'

with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
    content = source.read()
    destination.write(content)