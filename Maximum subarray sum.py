def maxSequence(arr):
    res = 0
    if len(arr) > 0:
        curr = arr[0]
        res = curr
        for i in range(1, len(arr)):
            el = arr[i]
            if curr + el > el:
                curr += el
            else:
                curr = el
            if res < curr:
                res = curr
    return res

print(maxSequence([]))