#埃氏筛，
"""def eratosthenes_sieve(n):
    if n < 2:
        return []

    is_prime = [True]*n
    #Zero and one are not prime
    is_prime[0] = is_prime[1] = False
    for i in range(2 , int(n**5)+1 , 1):
    #还没有被筛掉，是质数
        if is_prime[i] == True:
            #标记他的倍数为合数
            for j in range(i**2 , n , i):
                is_prime[j]= False
    return is_prime

def liner_sieve(n):
    pass
"""
import math
def is_prime(num):
    if num==1:
        return False
    if num==2:
        return True
    element=int(math.sqrt(num))+1
    for i in range(2,element+1,1):
        if num%i == 0:
            return False
    return True
def main():
    num=int(input())
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


if __name__ == "__main__":
    main()
