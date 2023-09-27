def remove_whitespace(input_string):
    return ' '.join(input_string.split())

input_string = "    Hello     Word"
print(remove_whitespace(input_string))