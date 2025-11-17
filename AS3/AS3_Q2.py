import re
class ComplexNumber:
    def __init__(self,complex_number):
        pattern = r'^\s*'  #开头空格
        pattern += r'((?P<real_sign>[+-])?'  # 实部符号
        pattern += r'(?P<real_num>\d+(\.\d+)?))?'  # 实部数值
        pattern += r'((?P<imag_sign>[+-])'  # 虚部符号
        pattern += r'(?P<imag_num>\d+(\.\d+)?))?i\s*$|^\s*'  # 虚部数值
        pattern += r'((?P<real_only_sign>[+-])?'  # 纯实数符号
        pattern += r'(?P<real_only_num>\d+(\.\d+)?))\s*$'  # 纯实数数值
        match = re.match(pattern, complex_number)
        if not match:
            raise ValueError
        if match.group('real_only_num'):
            real_sign = match.group('real_only_sign') or '+'
            real = float(f"{real_sign}{match.group('real_only_num')}")
            self.real = real
            self.imag = 0.0
        else:
            #是复数，处理实部
            real_sign = match.group('real_sign') or '+'
            real_num = match.group('real_num')
            real = float(f"{real_sign}{real_num}") if real_num else 0.0

            # 处理虚部
            imag_sign = match.group('imag_sign') or '+'
            imag_num = match.group('imag_num') or '1'  # 虚部无数值时添加1
            imag = float(f"{imag_sign}{imag_num}")
            self.real = real
            self.imag = imag

    def __add__(self,another):
        if self.imag + another.imag < 0:
            return f"{self.real + another.real}{self.imag + another.imag}i"
        elif self.imag + another.imag == 0:
            return f"{self.real + another.real}"
        else:
            return f"{self.real + another.real}+{self.imag + another.imag}i"
    def __sub__(self,another):
        if self.imag + another.imag < 0:
            return f"{self.real - another.real}{self.imag - another.imag}i"
        elif self.imag + another.imag == 0:
            return f"{self.real - another.real}"
        else:
            return f"{self.real - another.real}+{self.imag - another.imag}i"
    def __mul__(self,another):
        if self.real * another.imag + self.imag * another.real < 0:
            return f"{self.real * another.real - self.imag * another.imag}{self.real * another.imag + self.imag * another.real}i"
        elif self.real * another.imag + self.imag * another.real == 0:
            return f"{self.real * another.real - self.imag * another.imag}"
        else:
            return f"{self.real * another.real - self.imag * another.imag}+{self.real * another.imag + self.imag * another.real}i"
    def __truediv__(self,another):
        if another.real == 0 and another.imag == 0:
            raise ZeroDivisionError
        if self.imag * another.real - self.real * another.imag < 0:
            return f"{(self.real * another.real + self.imag * another.imag)/(another.real ** 2 + another.imag **2)}{(self.imag * another.real - self.real * another.imag)/(another.real ** 2 + another.imag **2)}i"
        elif self.imag * another.real - self.real * another.imag == 0:
            return f"{(self.real * another.real + self.imag * another.imag)/(another.real ** 2 + another.imag **2)}"
        else:
            return f"{(self.real * another.real + self.imag * another.imag)/(another.real ** 2 + another.imag **2)}+{(self.imag * another.real - self.real * another.imag)/(another.real ** 2 + another.imag **2)}i"

def test():
    num1 = "3+4i"
    num2 = "1-2i"
    try:
        Num1 = ComplexNumber(num1)
        Num2 = ComplexNumber(num2)
    except ValueError:
        print("This is not a complex number")
        return
    print(f"Addition: {Num1 + Num2}" )
    print(f"Subtraction: {Num1 - Num2}")
    print(f"Multiplication: {Num1 * Num2}")
    try:
        print(f"Division: {Num1 / Num2}")
    except ZeroDivisionError:
        print("can not divide by zero")

if __name__ == "__main__":
    test()
