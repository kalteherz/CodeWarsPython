def find_it(seq):
    all_int = {}
    for i in seq:
        all_int[i] = all_int.get(i, 0) + 1
    for k, v in all_int.items():
        if v % 2 == 1:
            return k
