# import sys
# sys.setrecursionlimit(10000)
def exp_sum(n):
    ar = [[-1] * (n + 1) for i in range(n + 1)]
    def check(n, k):
        if ar[n][k] == -1:
            ar[n][k] = p(n, k)
        return ar[n][k]
    def p(n, k):
        if k == 0:
            if n == 0:
                return 1
            else:
                return 0
        if k > n:
            return check(n, n)
        else:
            return check(n, k - 1) + check(n - k, k)

    return p(n, n) if n >= 0 else 0

print(exp_sum(700))