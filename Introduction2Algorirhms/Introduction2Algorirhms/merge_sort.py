# -*- coding: utf-8 -*-
def merge_sort(A, p, r):
    if p < r - 1:
        q = int((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    '''
    A是需要归并的序列
    p是第一个序列起始位置，q是第一个序列结束的元素的后一个元素的序号，
    q是第二个序列起始位置，r是第二个序列结束的元素的后一个元素的序号。
    '''
    #不使用标志位，做额外的判断
    left = A[p:q]
    right = A[q:r]
    i = 0
    j = 0
    for k in range(p, r):
        if i < q - p and j < r - q:
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
        elif i < q - p:
            A[k] = left[i]
            i += 1
        elif j < r - q:
            A[k] = right[j]
            j += 1

if __name__ == '__main__':
    l = [1,3,2,6,5,7,4,8,0,9]
    merge_sort(l, 0, len(l))
    print(l)