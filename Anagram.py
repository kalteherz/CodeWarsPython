def listPosition(word):
    charArr = []
    for i in range(27):
        charArr.append(0)
    for ch in word:
        charArr[ord(ch) - ord('A')] += 1
    fact = []
    fact.append(1)
    for i in range(25):
        fact.append((i + 1) * fact[i])
    res = 1
    for i in range(len(word)):
        ch = word[i]
        for j in range(26):
            if (charArr[j] > 0) & (ord(ch) > (j + ord('A'))):
                charArr[j] -= 1
                div = 1
                for k in range(26):
                    if charArr[k] > 1:
                        div *= fact[charArr[k]]
                res += fact[len(word) - i - 1] // div
                charArr[j] += 1
        charArr[ord(ch) - ord('A')] -= 1

    return res

print(listPosition("ABAB"))