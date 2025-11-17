class Matric:
    def __init__(self,a0,a1,b0,b1):
        self.matric=[[a0,a1],[b0,b1]]
    def __add__(self,another):
        return [[self.matric[0][0] + another.matric[0][0],self.matric[0][1] +another.matric[0][1]],
                [self.matric[1][0] + another.matric[1][0],self.matric[1][1] + another.matric[1][1]]]
    def __sub__(self,another):
        return [[self.matric[0][0] - another.matric[0][0],self.matric[0][1] - another.matric[0][1]],
                [self.matric[1][0] - another.matric[1][0],self.matric[1][1] - another.matric[1][1]]]
    def __mul__(self,another):
        return [[self.matric[0][0] * another.matric[0][0] + self.matric[0][1] * another.matric[1][0],
                self.matric[0][0] * another.matric[0][1] + self.matric[0][1] * another.matric[1][1]],
                [self.matric[1][0] * another.matric[0][0] + self.matric[1][1] * another.matric[1][0],
                self.matric[1][0] * another.matric[0][1] + self.matric[1][1] * another.matric[1][1]]]
    def calculate(self):
        return self.matric[0][0]*self.matric[1][1] - self.matric[0][1] *self.matric[1][0]

def test():
    matrix1 = Matric(1,2,3,4)
    matrix2 = Matric(5,6,7,8)
    #print(matrix1 + matrix2)
    print(f"matrix1 + matrix2 resulting in {matrix1 + matrix2}")
    print(f"matrix1 - matrix2 resulting in {matrix1 - matrix2}")
    print(f"matrix1 * matrix2 resulting in {matrix1 * matrix2}")
if __name__ == "__main__":
    test()
