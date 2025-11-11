def character_frequency(characters):
    dic = {}
    for element in characters:
        if element not in dic.get(characters.count(element), []):
            dic[characters.count(element)] = dic.get(characters.count(element), []) + [element]
    return dict(sorted(dic.items()))

def test():
    print(character_frequency("dddddcaabb"))

if __name__ == "__main__":
    test()