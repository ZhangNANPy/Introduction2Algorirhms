# -*- coding: utf-8 -*-
import matrixDot

def Fibonacci(n):
    if n < 0:
        return False
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        res = matrixPower([[1, 1], [1, 0]], n - 1)
    return res[0][0]

def matrixPower(matrix, n):
    if len(matrix) != len(matrix[0]):#注意这个判断不严谨，不能判断出行元素数不同的情况。
        raise  matrixDot.MatrixLengthError(len(matrix), len(matrix[0]))
    if n == 1:
        return matrix
    a = matrixPower(matrix, int(n / 2))
    res = matrixDot.matrixDot(a, a)
    if n % 2 == 0:
        return res
    else:
        res1 = matrixDot.matrixDot(res, matrix)
        return res1

if __name__ == '__main__':
    for i in range(100):
        print(Fibonacci(i))