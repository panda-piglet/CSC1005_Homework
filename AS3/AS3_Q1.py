def creat_matrix(*args):
    args = list(map(float,args))
    dimention = len(args)**0.5
    if int(dimention) != dimention:
        raise ValueError
    dimention = int(dimention)
    matrix = [[args[dimention*j + i] for i in range(dimention)]for j in range(dimention)]
    return matrix

class DoubleDimentionMatrix:
    def __init__(self,matrix):
        self.dimention = len(matrix)
        self.matrix = matrix
    def __repr__(self):
        return str(self.matrix)
    def __add__(self,another):
        return DoubleDimentionMatrix([[self.matrix[0][0] + another.matrix[0][0],self.matrix[0][1] +another.matrix[0][1]],
                [self.matrix[1][0] + another.matrix[1][0],self.matrix[1][1] + another.matrix[1][1]]])
    def __sub__(self,another):
        return DoubleDimentionMatrix([[self.matrix[0][0] - another.matrix[0][0],self.matrix[0][1] - another.matrix[0][1]],
                [self.matrix[1][0] - another.matrix[1][0],self.matrix[1][1] - another.matrix[1][1]]])
    def __mul__(self,another):
        return DoubleDimentionMatrix([[self.matrix[0][0] * another.matrix[0][0] + self.matrix[0][1] * another.matrix[1][0],
                self.matrix[0][0] * another.matrix[0][1] + self.matrix[0][1] * another.matrix[1][1]],
                [self.matrix[1][0] * another.matrix[0][0] + self.matrix[1][1] * another.matrix[1][0],
                self.matrix[1][0] * another.matrix[0][1] + self.matrix[1][1] * another.matrix[1][1]]])
    def calculate(self):
        return self.matrix[0][0]*self.matrix[1][1] - self.matrix[0][1] *self.matrix[1][0]

def test():
    matrix1 = DoubleDimentionMatrix(creat_matrix(1,2,3,4))
    matrix2 = DoubleDimentionMatrix(creat_matrix(5,6,7,8))
    #print(matrix1 + matrix2)
    print(f"matrix1 + matrix2 resulting in {matrix1 + matrix2}")
    print(f"matrix1 - matrix2 resulting in {matrix1 - matrix2}")
    print(f"matrix1 * matrix2 resulting in {matrix1 * matrix2}")
    #print(creat_matrix(1,2,3,4))
if __name__ == "__main__":
    test()
