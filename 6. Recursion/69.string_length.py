def string_length(input_string):
    if input_string == '':
        return 0
    else:
        return 1 + string_length(input_string[1:])
    
result = string_length("Hello")
print(f"The length is: {result}")