# -*- coding: utf-8 -*-
#给出k种硬币不限制使用数量，和给定的数额m，求组成这个数额的最少硬币数目。
def minCoins(coinList, money):#动态规划解法
    infinity = int(money / min(coinList)) + 2
    res = [[infinity for j in range(len(coinList) + 1)] for i in range(money + 1)]
    for i in range(len(coinList) + 1):
        res[0][i] = 0
    for i in range(1, money + 1):
        for j in range(1, len(coinList) + 1):
            if coinList[j - 1] <= i: 
                res[i][j] = min(res[i][j - 1], res[i % coinList[j - 1]][j - 1] + int(i / coinList[j - 1]))
            else: 
                res[i][j] = res[i][j - 1]
    if res[money][len(coinList)] >= infinity:
        return None
    else:
        return res[money][len(coinList)]

def minCoinsSimple(l, m):
    res = 0
    minCoin = min(l)
    while m != 0 and l != [] and m >= minCoin:
        maxIndex = 0
        for i in range(len(l)):
            if l[i] > l[maxIndex]:
                maxIndex = i
        res += int(m / l[maxIndex])
        m = m % l[maxIndex]
        del l[maxIndex]
    if m == 0:
        return res
    else:
        return None

if __name__ == '__main__':
    for i in range(20):
        if minCoins([1, 2, 4], i) == minCoinsSimple([1, 2, 4], i):
            print(True)
        else:
            print('minCoins =' + minCoins([1, 2, 4], i))
            print('minCoinsSimple =' + minCoinsSimple([1, 2, 4], i))