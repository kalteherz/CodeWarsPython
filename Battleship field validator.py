def validateBattlefield(field):
    ships = {}

    new_field = list(field)

    all = 0

    def not_empty(x, y):
        if (x < 0) | (y < 0) | (x >= 10) | (y >= 10):
            return False
        return new_field[x][y] == 1

    for x in range(10):
        for y in range(10):
            if not_empty(x, y):
                if (not_empty(x + 1, y) | not_empty(x - 1, y)) & (not_empty(x, y + 1) | not_empty(x, y - 1)) | not_empty(x + 1, y + 1) | not_empty(x - 1, y - 1) | not_empty(x + 1, y - 1) | not_empty(x - 1, y + 1):
                    return False

    def ship_calc(x, y):
        res = 0
        nx = x
        ny = y
        while not_empty(nx, ny):
            res += 1
            new_field[nx][ny] = 0
            nx += 1
        nx = x
        ny = y + 1
        while not_empty(nx, ny):
            res += 1
            new_field[nx][ny] = 0
            ny += 1
        return res

    for x in range(10):
        for y in range(10):
            if not_empty(x, y):
                ship_type = ship_calc(x, y)
                all += ship_type
                ships[str(ship_type)] = ships.get(str(ship_type), 0) + 1

    return (ships.get('4', 0) == 1) & (ships.get('4', 0) == 1) & (ships.get('3', 0) == 2) & (ships.get('2', 0) == 3) & (ships.get('1', 0) == 4) & (all == 20)


battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(validateBattlefield(battleField))