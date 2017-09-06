# -*- coding: utf-8 -*-

def InsertionSort(l, flag=True):
    for i in range(1, len(l)):
        key = l[i]
        for j in range(i - 1, -1, -1):
            if l[j] > key:
                l[j + 1] = l[j]
            else:
                break
        l[j + 1] = key
    if not flag:
        l.reverse()

if __name__ == '__main__':
    l = [1,4,3,6,8,3]
    InsertionSort(l, False)
    print(l)