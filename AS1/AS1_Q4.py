import math
def main():
    num=input()
    if "." in num:
        print("Illegal input!")
    else:
        num = int(num)
        if num < 0:
            print("Illegal input!")
        else:
            factorial = math.factorial(num)
            """if num == 0:
                pass
            else:
                for i in range(1,num+1,1):
                    factorial *= i"""
            print (f"The factorial of {num} is: {factorial}")


if __name__ == "__main__":
    main()
