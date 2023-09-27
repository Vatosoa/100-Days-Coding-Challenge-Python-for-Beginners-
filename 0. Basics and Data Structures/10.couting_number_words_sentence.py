def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "This is a sample sentence."
print(count_words(sentence))