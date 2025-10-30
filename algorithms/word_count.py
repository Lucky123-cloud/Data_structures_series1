def count_words(sentence):
    words = sentence.lower().split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# Example usage:
print(count_words("I love coding because I love problem solving"))