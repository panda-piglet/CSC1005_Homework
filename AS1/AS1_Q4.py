import math
def parse_positive_int(s):
    s=s.strip()
    if s.startswith('0'):
        raise ValueError
    elif not s.isdigit():
        raise ValueError
    n=int(s)
    return n

def main():
    num=input()
    try:
        num=parse_positive_int(num)
    except ValueError:
        print("Illegal input!")
    else:
        
        factorial = math.factorial(num)
        print (f"The factorial of {num} is: {factorial}")


if __name__ == "__main__":
    main()
