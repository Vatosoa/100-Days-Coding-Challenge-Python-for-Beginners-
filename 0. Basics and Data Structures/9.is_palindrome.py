def is_palindrome(input_string):
    return input_string == input_string[::-1]

input_string = "radar"
print(f"{input_string} = {input_string[::-1]} : {is_palindrome(input_string)}")
