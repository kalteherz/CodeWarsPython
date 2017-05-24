def narcissistic(value):
    tmp = value
    res = 0
    while tmp > 0:
        d = tmp % 10
        tmp //= 10
        res += pow(d, len(str(value)))
    return res == value