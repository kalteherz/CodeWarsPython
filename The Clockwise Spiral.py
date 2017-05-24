def createSpiral(n):
    res = []
    if not n.__class__ == int:
        return res
    if n < 1:
        return res
    for i in range(n):
        line = []
        for i in range(n):
            line.append(1)
        res.append(line)
    x = -1
    y = 0
    dx = 1
    dy = 0
    top = 1
    left = 0
    right = n - 1
    bottom = n - 1
    for i in range(n * n):
        x += dx
        y += dy
        res[y][x] = i + 1
        if (x == right) & (dx == 1):
            dx = 0
            dy = 1
            right -= 1
        if (y == bottom) & (dy == 1):
            dx = -1
            dy = 0
            bottom -= 1
        if (x == left) & (dx == -1):
            dx = 0
            dy = -1
            left += 1
        if (y == top) & (dy == -1):
            dx = 1
            dy = 0
            top += 1
    return res

print((createSpiral(4)))