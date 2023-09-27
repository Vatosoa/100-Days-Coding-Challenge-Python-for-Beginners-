def count_vowels_consonants(input_string):
    vowels = 'aeiouAEIOU'
    num_vowels = sum(1 for char in input_string if char in vowels)
    num_consonants = len(input_string) - num_vowels
    return num_vowels, num_consonants

input_string = "Hello World"
vowels, consonants = count_vowels_consonants(input_string)
print("Vowels: ", vowels)
print("Consonants: ", consonants)