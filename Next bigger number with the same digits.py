def next_bigger(n):
    nstr = str(n)
    i = len(nstr) - 2
    while i >= 0:
        j = i + 1
        min = -1
        while j < len(nstr):
            if int(nstr[j]) > int(nstr[i]):
                if (min == -1) | (int(nstr[min]) > int(nstr[j])):
                    min = j
            j += 1
        if not min == -1:
            lst = list(nstr)
            lst[i] = nstr[min]
            lst[min] = nstr[i]
            res = "".join(lst)[:i + 1]
            nxt = list("".join(lst)[i + 1:])
            nxt.sort()
            res += "".join(nxt)
            return int(res)
        i -= 1
    return -1

print(next_bigger(12))
print(next_bigger(513))
print(next_bigger(2017))
print(next_bigger(414))
print(next_bigger(144))
print(next_bigger(9))
print(next_bigger(111))
print(next_bigger(59884848459853))
