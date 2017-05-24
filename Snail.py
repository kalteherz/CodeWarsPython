def snail(array):
    n = len(array[0])
    res = []
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
        res.append(array[y][x])
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


array = [[]]
print(snail(array))