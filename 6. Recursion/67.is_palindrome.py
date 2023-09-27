def is_palindrome(input_string):
    cleaned_string = ''.join(e for e in input_string if e.isalnum()).lower()
    if len(cleaned_string) <= 1:
        return True
    else:
        return cleaned_string[0] == cleaned_string[-1] and is_palindrome(cleaned_string[1:-1])
    
result = is_palindrome("A man, a plan, a canal: Panama")
print(result)