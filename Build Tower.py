def tower_builder(n_floors):
    tow = []
    for i in range(n_floors):
        stars = ''.join(['*'] * (2 * i + 1))
        spaces = ''.join([' '] * (n_floors - i - 1))
        tow.append(spaces + stars + spaces)
    return tow

print(tower_builder(1))