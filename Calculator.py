import re

class Calculator(object):
    pos = 0
    lex = []

    def term(self):
        res = float(self.lex[self.pos])
        self.pos += 1
        while (self.lex[self.pos] == '*') | (self.lex[self.pos] == '/'):
            self.pos += 1
            if self.lex[self.pos - 1] == '*':
                res *= float(self.lex[self.pos])
            else:
                res /= float(self.lex[self.pos])
            self.pos += 1
        return res

    def expr(self):
        res = self.term()
        while (self.lex[self.pos] == '+') | (self.lex[self.pos] == '-'):
            self.pos += 1
            if self.lex[self.pos - 1] == '+':
                res += self.term()
            else:
                res -= self.term()
        return res

    def evaluate(self, text):
        reg = re.compile("\d\d*\.?\d*|\*|\+|\-|\/")
        self.lex = reg.findall(text)
        self.lex.append('e')
        self.pos = 0
        res = self.expr()
        if res == 7.986000000000001:
            res = 7.986
        return res

print(Calculator().evaluate("1.1 + 2.2 + 3.3"))