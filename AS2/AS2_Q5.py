def creat_bucket(pattern):
    bucket = [0 for i in range(128)]
    for element in pattern:
        bucket[ord(element)] +=1
    return bucket

def character_frequency(pattern):
    result={}
    bucket = creat_bucket(pattern)
    for i in range(0,128,1):
        if bucket[i] != 0 and result.get(bucket[i]) == None:
            result[bucket[i]] = [chr(i)]
        elif bucket[i] != 0:
            result[bucket[i]].append(chr(i))
    return dict(sorted(result.items()))

def test():
    example = "dddddcaabb"
    print(character_frequency(example))

if __name__ == "__main__":
    test()
    
#dict(sorted(grouped.items()))
