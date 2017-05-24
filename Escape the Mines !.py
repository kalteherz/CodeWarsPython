def solve(map, miner, exit):
    path = []

    width = len(map)
    height = len(map[0])

    was = []
    for i in range(width):
        was_line = []
        for j in range(height):
            was_line.append(False)
        was.append(was_line)

    def find(pos):
        if (pos['x'] == exit['x']) & (pos['y'] == exit['y']):
            return True
        if (pos['x'] < 0) | (pos['y'] < 0) | (pos['x'] >= width) | (pos['y'] >= height):
            return False
        if (not map[pos['x']][pos['y']]):
            return False
        if was[pos['x']][pos['y']]:
            return False

        was[pos['x']][pos['y']] = True

        path.append('right')
        if find({'x' : pos['x'] + 1, 'y' : pos['y']}):
            return True
        path.pop()

        path.append('left')
        if find({'x': pos['x'] - 1, 'y': pos['y']}):
            return True
        path.pop()

        path.append('up')
        if find({'x': pos['x'], 'y': pos['y'] - 1}):
            return True
        path.pop()

        path.append('down')
        if find({'x': pos['x'], 'y': pos['y'] + 1}):
            return True
        path.pop()

        was[pos['x']][pos['y']] = False

    find(miner)

    return path

minemap = [[True], [True], [True], [True]]

print(solve(minemap, {'x':0,'y':0}, {'x':3,'y':0}))