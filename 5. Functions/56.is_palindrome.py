def is_palindrome(input_string):
    cleaned_string = ''.join(e for e in input_string if e.isalnum()).lower()
    return cleaned_string == cleaned_string[::-1]

result = is_palindrome("A man, a plan, a canal: Panama")
print(result)
