#作弊方法
def cheat():
    perfect_numbers=[6,28,496,8128,33550336,8589869056,137438691328]
    maxrange=input()
    if "."in maxrange or int(maxrange) <= 0:
        print("Illegal input!")
    else:
        maxrange=int(maxrange)
        print(f"The perfect numbers smaller than {maxrange} are:")
        for element in perfect_numbers:
            if element < maxrange:
                print(element)
#枚举方法
def main():
    maxrange=input()
    if "."in maxrange or int(maxrange) <= 0:
        print("Illegal input!")
    else:
        maxrange=int(maxrange)
        print(f"The perfect numbers smaller than {maxrange} are:")
        #一层循环枚举所有小于maxrange的数并判断是否为完全数
        for i in range(1,maxrange+1,1):
            sum=0
            #二层循环找i的所有因数
            for j in range(1,i,1):
                if i%j==0:
                    sum += j
            if sum == i:
                print(sum)

if __name__=="__main__":
    main()
