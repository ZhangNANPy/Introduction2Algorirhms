# -*- coding: utf-8 -*-
import random
def partition(l, begin, end):
    x = l[end - 1]
    i = begin - 1
    for j in range(begin, end - 1):
        if l[j] <= x:
            i += 1
            (l[i], l[j]) = (l[j], l[i])
    (l[end - 1], l[i + 1]) = (l[i + 1], l[end - 1])
    return i + 1

def quickSort(l, begin, end):
    if begin < end:
        q = partition(l, begin, end)
        quickSort(l, begin, q)
        quickSort(l, q + 1, end)

def randomizedPartition(l, begin, end):
    i = random.randint(begin, end - 1)
    (l[i], l[end - 1]) = (l[end - 1], l[i])
    return partition(l, begin, end)

def randomQuickSort(l, begin, end):
    if begin < end:
        q = randomizedPartition(l, begin, end)
        randomQuickSort(l, begin, q)
        randomQuickSort(l, q + 1, end)

if __name__ == '__main__':
    a = [1,5,4,7,6,3,4,2]
    randomQuickSort(a, 0, len(a))
    print(a)