def get_pins(observed):
    num = {'0': ['0', '8'],
           '1': ['1', '2', '4'],
           '2': ['2', '1', '3', '5'],
           '3': ['3', '2', '6'],
           '4': ['4', '1', '5', '7'],
           '5': ['5', '2', '4', '6', '8'],
           '6': ['6', '3', '5', '9'],
           '7': ['7', '8', '4'],
           '8': ['8', '5', '7', '9', '0'],
           '9': ['9', '6', '8']}
    res = []
    elem = []
    def gen(pos):
        if pos == len(observed):
            res.append("".join(elem))
            return
        for n in num[observed[pos]]:
            elem.append(n)
            gen(pos + 1)
            elem.pop()
    gen(0)
    return res

print(sorted(get_pins('369')))