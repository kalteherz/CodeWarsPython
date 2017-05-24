import math

def validSolution(ar):
    n = len(ar[0])
    if not n == 9:
        return False
    for line in ar:
        if not n == len(line):
            return False
    for i in range(n):
        row = {}
        col = {}
        for j in range(n):
            if row.get(ar[i][j]) is None:
                row[ar[i][j]] = 1
            else:
                return False
            if col.get(ar[j][i]) is None:
                col[ar[j][i]] = 1
            else:
                return False
    nn = math.trunc(math.sqrt(n))
    for i in range(nn):
        x = i * nn
        for j in range(nn):
            y = j * nn
            sq = {}
            for dx in range(nn):
                for dy in range(nn):
                    cel = ar[x + dx][y + dy]
                    if not type(cel) is int:
                        return False
                    if (cel < 1) or (cel > n):
                        return False
                    if sq.get(cel) is None:
                        sq[cel] = 1
                    else:
                        return False
    return True