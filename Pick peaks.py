def pick_peaks(arr):
    i = 1
    res = {'pos' : [], 'peaks' : []}
    while i < len(arr) - 1:
        if arr[i] > arr[i - 1]:
            if arr[i] > arr[i + 1]:
                res['pos'].append(i)
                res['peaks'].append(arr[i])
            elif arr[i] == arr[i + 1]:
                pos = i
                while (i < len(arr) - 1) & (arr[pos] == arr[i]):
                    i += 1
                if arr[i] < arr[pos]:
                    res['pos'].append(pos)
                    res['peaks'].append(arr[pos])
                else:
                    i -= 1
        i += 1
    return res

print(pick_peaks([19, -1, 7, 18, 3, -3, -4, -4, 1, 2, 15, 3, -3, 15, 17, 16, 1, 4, 4, 7, 3, 11, 20]))