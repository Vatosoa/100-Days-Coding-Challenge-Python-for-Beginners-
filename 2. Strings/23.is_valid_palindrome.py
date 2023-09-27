def is_valid_palindrome(input_string):
    cleaned_string = ''.join(e for e in input_string if e.isalnum()).lower()
    print(cleaned_string)
    print(cleaned_string[::-1])
    return cleaned_string == cleaned_string[::-1]

input_string = "A man, a plan, a canal: Panama"
print(is_valid_palindrome(input_string))