import string
def to_postfix (infix):
    pass
    prior = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    st = []
    res = []
    for ch in infix:
        if ch in string.digits:
            res.append(ch)
        elif ch == '(':
            st.append(ch)
        elif ch == ')':
            while True:
                op = st.pop()
                if not op == '(':
                    res.append(op)
                else:
                    break
        else:
            if ch == '^':
                st.append(ch)
            else:
                while (len(st) > 0) and (prior[ch] <= prior[st[-1]]):
                    res.append(st.pop())
                st.append(ch)
    while len(st) > 0:
        res.append(st.pop())
    return "".join(res)