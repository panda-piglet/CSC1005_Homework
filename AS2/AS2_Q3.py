def quick_sort(pattern):
    if len(pattern) <=1:
        return pattern
    left = []
    middle = []
    right = []
    base = pattern[len(pattern) // 2]
    for element in pattern :
        if element < base:
            left.append(element)
        elif element > base:
            right.append(element)
        else:
            middle.append(element)
    return quick_sort(left) + middle +quick_sort(right)

def group_anagrams(lis):
    result = []
    for element in lis:
        if len(result) == 0:
            result.append([element])
        else:
            for group in result:
                if quick_sort(group[0]) == quick_sort(element):
                    group.append(element)
                    break
            else:
                result.append([element])
    return result
def test():
    example = ["listen","silent","enlist","rat","tar","god","dog","evil","vile","veil"]
    print (group_anagrams(example))

if __name__ == "__main__":
    test()
