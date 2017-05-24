def bubble(l):
    res = []
    for i in range(len(l)):
        for j in range(1, len(l)):
            if l[j - 1] > l[j]:
                tmp = l[j - 1]
                l[j - 1] = l[j]
                l[j] = tmp
                res.append(list(l))
    return res

l=[1,4,3,6,7,9,2,5,8]
print(bubble(l))