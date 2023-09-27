def capitalize_words(input_string):
    words = input_string.split()
    capitalized_word = [word.capitalize() for word in words]
    return ' '.join(capitalized_word)

input_string = "hello world"
print(capitalize_words(input_string))