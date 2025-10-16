#判断质数
def is_prime(x):
    if x < 2: return False
    if x % 2 == 0:
        return x == 2
    division = 3 
    root = int(x**0.5)
    while division <= root:
        if x % division == 0: 
            return False
        division += 2
    return True

def main():
    num=int(input())
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()
