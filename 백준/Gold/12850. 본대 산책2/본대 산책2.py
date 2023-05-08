mod = 1000000007

class Matrix:
    def __init__(self, array):
        self.array = array
        
    def __mul__(self, other):
        result = [[0] * 8 for _ in range(8)]
        for i in range(8):
            for k in range(8):
                for j in range(8):
                    result[i][j] = (result[i][j] + self.array[i][k] * other.array[k][j]) % mod
        return Matrix(result)
    
    def __pow__(self, power):
        result = Matrix([[0] * 8 for _ in range(8)])
        for i in range(8):
            result.array[i][i] = 1
        while power:
            if power % 2:
                result *= self
            self *= self
            power //= 2
        return result

Base = Matrix([
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
])

D = int(input())
Base = Base ** D

print(Base.array[0][0])
