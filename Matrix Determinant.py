import math

def determinant(matrix):
    n = len(matrix[0])
    if n == 1:
        return matrix[0][0]
    res = 0
    for i in range(n):
        minor = []
        for k in range(n):
            if not k == i:
                line = []
                for l in range(n):
                    if not l == 0:
                        line.append(matrix[k][l])
                minor.append(line)
        res += math.pow(-1, i) * matrix[i][0] * determinant(minor)
    return res

m1 = [[1, 3], [2,5]]
m2 = [[2,5,3], [1,-2,-1], [1, 3, 4]]

print(determinant([[1]]))
print(determinant(m1))
print(determinant(m2))