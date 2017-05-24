def lcs(x, y):
    if (x == '') or (y == ''):
      return ''
    ar = [[0] * (len(y) + 1) for i in range(len(x) + 1)]
    for ii in range(len(ar)):
        i = len(ar) - ii - 1
        for jj in range(len(ar[0])):
            j = len(ar[0]) - jj - 1
            if (ii == 0) or (jj == 0):
                ar[i][j] = 0
            elif x[i] == y[j]:
                ar[i][j] = ar[i + 1][j + 1] + 1
            else:
                ar[i][j] = max(ar[i + 1][j], ar[i][j + 1])
    res = ''
    i = j = 0
    while (i < len(x)) and (j < len(y)):
        if x[i] == y[j]:
            res += x[i]
            i += 1
            j += 1
        elif ar[i + 1][j] >= ar[i][j + 1]:
            i += 1
        else:
            j += 1
    return res

print(lcs("abcdef" , "abc"))