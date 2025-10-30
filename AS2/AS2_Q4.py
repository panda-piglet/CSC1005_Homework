def generate_rotated_words(word):
    result = [word]
    rotated_word = word
    for i in range(len(word) - 1):
        rotated_word = rotated_word[1::] + rotated_word[0]
        result.append(rotated_word)
    return result

def group_rotated_words(lis):
    result = []
    for word in lis:
        if len(result) == 0:
            result.append(sorted(generate_rotated_words(word)))
        else:
            for group in result:
                if word in group:
                    break
            else:
                result.append(sorted(generate_rotated_words(word)))
    return result
def test():
    example = ["hello","ohell","lohel","elloh","world"]
    print(group_rotated_words(example))

if __name__ == "__main__":
    test()
