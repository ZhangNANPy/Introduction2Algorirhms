# -*- coding: utf-8 -*-
import sys
def maxCrossingSubarray(l, low, mid, high):
    maxSum = 0
    lSum = -sys.maxsize #sys.maxsize是系统中最大整数
    for i in range(mid - 1, low - 1, -1):
        maxSum = maxSum + l[i]
        if maxSum > lSum:
            lSum = maxSum
            maxLeft = i

    maxSum = 0
    rSum = -sys.maxsize
    for i in range(mid, high):
        maxSum = maxSum + l[i]
        if maxSum > rSum:
            rSum = maxSum
            maxRight = i
    return (maxLeft, maxRight + 1, lSum + rSum)

def maxSubarray(l, low, high):
    if low == high - 1:
        return (low, high, l[low])
    else:
        mid = int((low + high) / 2)
        (ll, lh, ls) = maxSubarray(l, low, mid)
        (rl, rh, rs) = maxSubarray(l, mid, high)
        (cl, ch, cs) = maxCrossingSubarray(l, low, mid, high)
        if ls >= rs and ls >= cs:
            return (ll, lh, ls)
        elif rs >= ls and rs >= cs:
            return (rl, rh, rs)
        else:
            return (cl, ch, cs)

def maxSubarrayline(l, n):
    sum = -sys.maxsize
    temp = -sys.maxsize
    for i in range(n):
        if temp < 0:
            temp = l[i]
            leftTemp = i
            rightTemp = i + 1
        else:
            temp += a[i]
            rightTemp = i + 1
        if sum < temp:
            sum = temp
            left = leftTemp
            right = rightTemp
    return (left, right, sum)

if __name__ == '__main__':
    a = [1,-3,5,-2,6,-44,7,-3]
    print(maxSubarray(a, 0, len(a)))
    print(maxSubarrayline(a, len(a)))