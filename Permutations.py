def permutations(text):
    let = {}
    for ch in text:
        let[ch] = let.get(ch, 0) + 1
    res = {}

    elem = list(text)
    def gen(pos):
        if pos == len(text):
            res[''.join(elem)] = 1
            return
        for ch in let:
            if let[ch] > 0:
                elem[pos] = ch
                let[ch] -= 1
                gen(pos + 1)
                let[ch] += 1

    gen(0)
    return res.keys()


print(sorted(permutations('abc')))