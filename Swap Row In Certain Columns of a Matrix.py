def swap(matrix, row1, row2, *columns):
    for i in columns:
        matrix[row1][i], matrix[row2][i] = matrix[row2][i], matrix[row1][i]
    return matrix

print(swap([[0, 1], [2, 3]], 0, 1, 0))