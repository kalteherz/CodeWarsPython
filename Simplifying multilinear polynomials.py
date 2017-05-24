import re

def str_comp(st1, st2):
    if len(st1) == len(st2):
        return st1 < st2
    else:
        return len(st1) < len(st2)

def simplify(poly):
    reg = re.compile('[\+\-]|\d\d*|[a-z][a-z]*')
    lexemes = reg.findall(poly)
    sign = 1
    mlt = 1
    calc_lex = {}
    for lex in lexemes:
        if lex == '+':
            sign = 1
        elif lex == '-':
            sign = -1
        elif lex[0] in '0123456789':
            mlt = int(lex)
        else:
            word = ''.join(sorted(list(lex)))
            calc_lex[word] = calc_lex.get(word, 0) + sign * mlt
            mlt = 1
    sortval = list(calc_lex.keys())
    for j in range(len(sortval)):
        for i in range(len(sortval) - 1):
            if str_comp(sortval[i + 1], sortval[i]):
                sortval[i + 1], sortval[i] = sortval[i], sortval[i + 1]
    res = ''
    first = True
    for lex in sortval:
        v = calc_lex[lex]
        if v != 0:
            if v > 0 and not first:
                res += '+'
            if v < 0:
                res += '-'
            if abs(v) != 1:
                res += str(abs(v))
            res += lex
            first = False
    return res

print(simplify("-a+5ab+3a-c-2a"))