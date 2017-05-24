def lcs(x, y):
    if (x == '') or (y == ''):
      return 0
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
    return ar[0][0]

def is_merge(s, part1, part2):
    l1 = lcs(s, part1)
    l2 = lcs(s, part2)
    alph = {}
    for ch in s:
        alph[ch] = alph.get(ch, 0) + 1
    def check(sub):
        for ch in sub:
            if alph.get(ch, 0) == 0:
                return False
            else:
                alph[ch] -= 1
        return True
    if not check(part1):
        return False
    if not check(part2):
        return False
    return ((l1 + l2) == len(s)) and (l1 == len(part1)) and (l2 == len(part2))

print(is_merge("Bananas from Bahamas", "Bahas", "Bananas from am"));
print(is_merge('codewars', 'codewars', ''));
print(not is_merge('codewars', 'cod', 'wars'))