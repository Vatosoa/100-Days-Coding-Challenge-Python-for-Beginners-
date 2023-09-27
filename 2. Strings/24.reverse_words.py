def reverse_words(sentence):
    words = sentence.split()
    reverse_words = ''.join(reversed(words))
    return reverse_words

sentence = "Hello world"
print(reverse_words(sentence))