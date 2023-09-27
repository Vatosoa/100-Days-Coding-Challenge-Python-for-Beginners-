def reverse_string(input_string):
    if len(input_string) == 0:
        return input_string
    else:
        return reverse_string(input_string[1:]) + input_string[0]
    
result = reverse_string("Hello")
print(result)