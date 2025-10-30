def format_output(lst):
    row = 1
    for element in lst:
        if row == 10:
            print(element)
            row = 0
        else:
            print(element,end=" ")
            row += 1

def reverse_number(num):
    num = int(str(num)[::-1])
    return num

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    d, r = 3, int(x**0.5)
    while d <= r:
        if x % d == 0:
             return False
        d += 2
    return True

def main():
    result = []
    numbers_required = int(input())
    root = 1
    while numbers_required != 0:
        possible_num = root**2
        if is_prime(reverse_number(possible_num)):
            result.append(possible_num)
            numbers_required -= 1
        root += 1
    format_output(result)

if __name__ == "__main__":
    main()
