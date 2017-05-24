def findSum(m):
    a = [[0] * len(m) for i in range(len(m))]
    a[0][0] = m[0][0]
    for i in range(len(m) - 1):
        a[0][i + 1] = a[0][i] + m[0][i + 1]
        a[i + 1][0] = a[i][0] + m[i + 1][0]
    for i in range(1, len(m)):
        for j in range(i, len(m)):
            a[i][j] = max(a[i - 1][j], a[i][j - 1]) + m[i][j]
            a[j][i] = max(a[j][i - 1], a[j - 1][i]) + m[j][i]
    return a[len(m) - 1][len(m) - 1]


matrix = [[20, 20, 10, 10],
          [10, 20, 10, 10],
          [10, 20, 20, 20],
          [10, 10, 10, 20]]
print(findSum(matrix))