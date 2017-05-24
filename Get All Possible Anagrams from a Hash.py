def get_words(hash_of_letters):
    let = {}
    ln = 0
    elem = []
    for k, v in hash_of_letters.items():
        for vv in v:
            let[vv] = k
            ln += k
            for j in range(k):
                elem.append(vv)
    res = {}

    def gen(pos):
        if pos == ln:
            res[''.join(elem)] = 1
            return
        for ch in let:
            if let[ch] > 0:
                elem[pos] = ch
                let[ch] -= 1
                gen(pos + 1)
                let[ch] += 1

    gen(0)
    return sorted(res.keys())

print(get_words({2:["a"], 1:["b", "c"]}))