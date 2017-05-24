def spiralize(size):
    spiral = []

    for i in range(size):
        spiralLine = []
        for i in range(size):
            spiralLine.append(0)
        spiral.append(spiralLine)

    def in_range(x, y):
        return (x >= 0) & (y >= 0) & (x < size) & (y < size)

    def is_zero(x, y):
        if not in_range(x, y):
            return True
        return spiral[y][x] == 0

    x = -1
    y = 0
    old_x = 0
    old_y = 0

    while (not x == old_x) | (not y == old_y):
        old_x = x
        old_y = y
        while in_range(x + 1, y) & is_zero(x + 2, y) & is_zero(x + 1, y + 1):
            x += 1
            spiral[y][x] = 1

        while in_range(x, y + 1) & is_zero(x, y + 2) & is_zero(x - 1, y + 1):
            y += 1
            spiral[y][x] = 1

        while in_range(x - 1, y) & is_zero(x - 2, y) & is_zero(x - 1, y - 1):
            x -= 1
            spiral[y][x] = 1

        while in_range(x, y - 1) & is_zero(x, y - 2) & is_zero(x + 1, y - 1):
            y -= 1
            spiral[y][x] = 1


    return spiral

spiralize(10)