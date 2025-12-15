def fast_pow(x, n):
    # 基准情形1：n=0时，任何数的0次幂为1
    if n == 0:
        return 1
    # 基准情形2：n=1时，结果为x本身
    if n == 1:
        return x
    # 递归拆分：计算x^(n//2)
    half = fast_pow(x, n // 2)
    # 分情况合并结果
    if n % 2 == 0:
        # n为偶数：(x^(n/2))^2
        return half * half
    else:
        # n为奇数：x * (x^((n-1)/2))^2
        return x * half * half
