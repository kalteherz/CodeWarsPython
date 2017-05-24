one = 1
zero = 0

def multiply(n, f):
    if n > f:
        a = n
        b = f
    else:
        a = f
        b = n
    res = a
    i = zero
    two = one + one
    while b > 0:
        if (b & one) == one:
            res += a
            b -= one
        else:
            res += res
            b = b >> two
    return res

print(multiply(7, 7))