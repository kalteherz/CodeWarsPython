res = 0

def count_change(money, coins):
    global res
    res = 0

    def calc(coin, rest):
        global res
        if coin == len(coins) - 1:
            if rest % coins[coin] == 0:
                res += 1
            return
        for i in range(rest // coins[coin] + 1):
            calc(coin + 1, rest - i * coins[coin])

    coins.sort(reverse=True)
    calc(0, money)
    return res

print(count_change(4, [1,2]))
print(count_change(10, [5,2,3]))
print(count_change(11, [5,7]))