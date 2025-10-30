def find_mirror_words(sentence):
    result = []
    words = sentence.split()
    for word in words:
        if word == word[::-1]:
            result.append(word)
    return result
