# -*- coding: utf-8 -*-
def countingSort(l, res, k):
    temp = [0 for i in range(k)]
    for i in l:
        temp[i] += 1
    for i in range(1, len(temp)):
        temp[i] += temp[i - 1]
    for i in range(len(l) - 1, -1, -1):
        res[temp[l[i]] - 1] = l[i]
        temp[l[i]] -= 1

if __name__ == '__main__':
    l = [2,5,3,0,2,3,0,3]
    res = l[:]
    countingSort(l, res, 6)
    print(res)