#这个文件用于介绍一下KMP算法
#用途是在一个长的字符串中寻找一个较短的字符串
#为方便，我们将长字符串称为文本串，短的字符串称为模式串

#这个函数的功能是计算前缀表
#前缀表存储的是{模式串的【（每一个前缀以及它本身）的最长相同的前缀与后缀】}的长度
def build_perfix_table(pattern):
     #第一个前缀只有一个字符，最长相同前后缀长度为0
    perfix_table=[0]
     #第一个前缀已经在列表中，我们从第二个前缀开始计算
    for perfix_tail in range(1,len(pattern),1):
         #切片取出被计算的前缀
        perfix=pattern[0:perfix_tail+1:1]
        longest_same_perfix_and_suffix=0
        for length in range(1 , len(perfix)//2 + 1 , 1):
            if perfix[0:length:1] == perfix[len(perfix)-length::]:
                longest_same_perfix_and_suffix += 1
            else:
                break
        perfix_table.append(longest_same_perfix_and_suffix)
    return perfix_table

def KMP_search(text,pattern):
    perfix_table = build_perfix_table(pattern)
    i=0 #text指针
    j=0 #pattern指针
    while i<len(text) and j < len(pattern):
        #
        if text[i] == pattern[j]:
            j += 1
            i += 1
        elif j==0:
            i += 1
        else:
            j = j-1-perfix_table[j-1]
    if j == len(pattern):
        return i-j
    else:
        return -1
        
def main():
    text = input()
    pattern = input()
    result = KMP_search(text,pattern)
    print(result)

def test():
    pattern = input()
    print(build_perfix_table(pattern))

if __name__ == "__main__":
    main()
