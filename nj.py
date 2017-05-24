checkSide = [0] * 2
for i in range(2):
    checkSide[i] = [0] * 50
inString = input()
nString = inString[0: inString.find(" ")]
kString = inString[inString.find(" ") + 1: len(inString)]
n = int(nString)
k = int(kString)
sides = ["", ""]
sides[0] = input()
sides[1] = input()
def jump(side, position):
    checkSide[side][position] = 1
    if position + k < n:
        if sides[1 - side][position + k] == "-":
            if checkSide[1 - side][position + k] == 0:
                jump(1 - side, position + k)
    if position < n - 1:
        if sides[side][position + 1] == "-":
            if checkSide[side][position + 1] == 0:
                jump(side, position + 1)
    if position > 0:
        if sides[side][position - 1] == "-":
            if checkSide[side][position - 1] == 0:
                jump(side, position - 1)
jump(0, 0)
canOut = False
for i in range(n):
    if checkSide[0][i] == 1 or checkSide[1][i] == 1:
        if i + 1 >= n or i + k >= n:
            canOut = True
if canOut:
    print("YES")
else:
    print("NO")