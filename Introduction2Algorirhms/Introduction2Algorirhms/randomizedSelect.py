# -*- coding: utf-8 -*-
from quickSort import randomizedPartition

def randomizedSelect(l, p, r, i):
    if p == r:
        return l[p]
    q = randomizedPartition(l, p, r)
    k = q - p + 1
    if i == k:
        return l[q]
    elif i < k:
        return randomizedSelect(l, p, q - 1, i)
    else:
        return randomizedSelect(l, q + 1, r, i - k)

if __name__ == "__main__":
    a = [0,1,2,3,4,5,6,7,8,9]
    print(randomizedSelect(a, 0, len(a), 4))