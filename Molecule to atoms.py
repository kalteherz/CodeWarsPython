import re
import string

pos = 0
def parse_molecule (formula):
    formula = "(" + formula + ")1"
    reg = re.compile("[A-Z][a-z]?|\[|\]|\(|\)|\{|\}|\d\d*")
    lexemes = reg.findall(formula)

    global pos
    pos = 0
    def calc():
        curr = {}
        global pos
        while pos < len(lexemes):
            lex = lexemes[pos]
            if lex[0] in string.ascii_letters:
                curr[lexemes[pos]] = curr.get(lexemes[pos], 0) + 1
            elif (lex[0] == '(') | (lex[0] == '[') | (lex[0] == '{'):
                pos += 1
                include = calc()
                for k in include:
                    curr[k] = curr.get(k, 0) + include[k]
            elif (lex[0] == ')') | (lex[0] == ']') | (lex[0] == '}'):
                if lexemes[pos + 1][0] in string.digits:
                    pos += 1
                    multi = int(lexemes[pos])
                    for k in curr:
                        curr[k] *= multi
                return curr
            else:
                curr[lexemes[pos - 1]] = curr.get(lexemes[pos - 1], 0) + int(lex) - 1
            pos += 1
        return curr

    return calc()

print(parse_molecule("K4[ON(SO3)2]2"))
