#处理非法输入并引发错误
def parse_positive_int(s):
    #strip 方法去除被操作字符串头尾含有参数中子串的字符
    #这里去除字符串头尾空格
    s=s.strip()
    if s.startswith('0'):
        raise ValueError
    elif not s.isdigit():
        raise ValueError
    n=int(s)
    return n
#判断质数
def is_prime(x):
    if x < 2: return False
    if x % 2 == 0:
        # 直接特判偶数，减少运算量
        #如果是偶数并且为2，返回真，否则为假
        return x == 2
    d, r = 3, int(x**0.5)
    while d <= r:
        if x % d == 0: return False
        d += 2
    return True

def main():
    try:
        N = parse_positive_int(input())
    except ValueError:
        print("Illegal input!")
        # return 没有返回值，用于终止函数，相当于sys.exit()
        return

    print(f"The perfect numbers smaller than {N} are:")
    p = 2
    while True:
        # << 为二进制位移操作，将十进制数转化为二进制后向左位移指定格数，剩下位置用0填充，再转化为十进制
        # 可以简单理解为乘2**p
        # 下面是梅森素数公式
        m = (1 << p) - 1
        n = (1 << (p - 1)) * m
        # 可能值大于范围，结束循环
        if n >= N:
            break
            #如果2**P-1是素数(指数P也是素数)，则2**(P-1)(2**P-1)是完全数。所有的偶完全数都有这种形式。
        if is_prime(m):
            print(n)
        p += 1

if __name__ == "__main__":
    main()
