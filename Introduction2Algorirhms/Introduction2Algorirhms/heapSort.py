# -*- coding: utf-8 -*-
'''
堆算法计数从1开始,有n-1个元素
最大堆性质:父大于子
'''
def parent(i):
    return int(i/2)
def left(i):
    return i*2
def right(i):
    return 2*i+1

def maxHeapify(heap, i, n):
    '''
    维护最大堆性质，调整堆中第i个元素到合适的位置
    n是堆中元素的数量
    '''
    l = left(i)
    r = right(i)
    if l <= n and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r <= n and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        (heap[i], heap[largest]) = (heap[largest], heap[i])
        maxHeapify(heap, largest, n)

def buildMaxHeap(heap, n):
    '''
    注意开始的位置，直接略过了叶子结点
    '''
    for i in range(int(n/2), 0, -1):
        maxHeapify(heap, i, n)

def heapSort(heap):
    buildMaxHeap(heap, len(heap) - 1)
    n = len(heap) - 1
    for i in range(n, 1, -1):
        (heap[1], heap[i]) = (heap[i], heap[1])
        n -= 1
        maxHeapify(heap, 1, n)

def heapMax(heap):
    return heap[1]

def heapExtractMax(heap):
    if len(heap) < 2:
        return None
    max = heap[1]
    heap[1] = heap[len(heap) - 1]
    del heap[len(heap) - 1]
    maxHeapify(heap, 1, len(heap) - 1)
    return max

def heapIncreaseKey(heap, i, key):
    '''
    把堆中编号为i的元素，增大到key
    '''
    if key < heap[i]:
        return None
    heap[i] = key
    while i > 1 and heap[parent(i)] < heap[i]:
        (heap[parent(i)], heap[i]) = (heap[i], heap[parent(i)])
        i = parent(i)

def maxHeapInsert(heap, key):
    heap.append(key)
    heapIncreaseKey(heap, len(heap) - 1, key)

if __name__ == "__main__":
    a = [-1, 3, 6,5,4,3,2,1]
    buildMaxHeap(a, len(a) - 1)
    maxHeapInsert(a, 7)
    print(a)