import re
def order_weight(text):
    reg = re.compile('\d\d*')
    lst = sorted(reg.findall(text))
    def dsum(s):
        res = 0
        for ch in s:
            res += int(ch)
        return res
    for j in range(len(lst)):
        for i in range(len(lst) - 1):
            if dsum(lst[i]) > dsum(lst[i + 1]):
                tmp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = tmp
    res = ''
    for e in lst:
        res += e + " "
    if res != '':
        res = res[:len(res) - 1]
    return res

print(order_weight("103 123 4444 99 2000"))