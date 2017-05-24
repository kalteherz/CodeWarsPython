import math

class Sudoku(object):
    def __init__(self, ar):
        self.ar = ar
        self.n = len(ar[0])

    def is_valid(self):
        if self.n < 1:
            return False
        if not math.trunc(math.sqrt(self.n)) - math.sqrt(self.n) == 0:
            return False
        for line in self.ar:
            if not self.n == len(line):
                return False
        for i in range(self.n):
            row = {}
            col = {}
            for j in range(self.n):
                if row.get(self.ar[i][j]) is None:
                    row[self.ar[i][j]] = 1
                else:
                    return False
                if col.get(self.ar[j][i]) is None:
                    col[self.ar[j][i]] = 1
                else:
                    return False
        nn = math.trunc(math.sqrt(self.n))
        for i in range(nn):
            x = i * nn
            for j in range(nn):
                y = j * nn
                sq = {}
                for dx in range(nn):
                    for dy in range(nn):
                        cel = self.ar[x + dx][y + dy]
                        if not type(cel) is int:
                            return False
                        if (cel < 1) or (cel > self.n):
                            return False
                        if sq.get(cel) is None:
                            sq[cel] = 1
                        else:
                            return False
        return True


goodSudoku1 = Sudoku([
    [7, 8, 4, 1, 5, 9, 3, 2, 6],
    [5, 3, 9, 6, 7, 2, 8, 4, 1],
    [6, 1, 2, 4, 3, 8, 7, 5, 9],

    [9, 2, 8, 7, 1, 5, 4, 6, 3],
    [3, 5, 7, 8, 4, 6, 1, 9, 2],
    [4, 6, 1, 9, 2, 3, 5, 8, 7],

    [8, 7, 6, 3, 9, 4, 2, 1, 5],
    [2, 4, 3, 5, 6, 1, 9, 7, 8],
    [1, 9, 5, 2, 8, 7, 6, 3, 4]
])

goodSudoku2 = Sudoku([
    [1, 4, 2, 3],
    [3, 2, 4, 1],

    [4, 1, 3, 2],
    [2, 3, 1, 4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
    [0, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],

    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
])

badSudoku2 = Sudoku([['hgh']])

print(goodSudoku1.is_valid())#, True, 'Testing valid 9x9')
print(goodSudoku2.is_valid())#, True, 'Testing valid 4x4')

print(badSudoku1.is_valid())#, False, 'Values in wrong order')
print(badSudoku2.is_valid())#, False, '4x5 (invalid dimension)')