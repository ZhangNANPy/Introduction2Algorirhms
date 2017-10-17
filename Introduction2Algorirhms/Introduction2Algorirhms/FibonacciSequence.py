# -*- coding: utf-8 -*-
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

def matrixPower(m, n):
    if len(m) != len(m[0]):#注意这个判断不严谨，不能判断出行元素数不同的情况。
        raise MatrixLengthError(len(m), len(m[0]))
    if n == 1:
        return m
    a = matrixPower(m, int(n / 2))
    res = [[0 for j in range(len(m[0]))] for i in range(len(m))]
    for row in range(len(res)):
            for column in range(len(res)):
                for k in range(len(a)):
                    res[row][column] += a[row][k] * a[k][column]
    if n % 2 == 0:
        return res
    else:
        res1 = [[0 for j in range(len(m[0]))] for i in range(len(m))]
        for row in range(len(res)):
            for column in range(len(res)):
                for k in range(len(m)):
                    res1[row][column] += res[row][k] * m[k][column]
        return res1

class MatrixLengthError(Exception):
    def __init__(self, n, m):
        self.m = m
        self.n = n
    def __str__(self):
        return repr('The number of matrix columns is not equal to the number of rows!\n' + str(self.n) + 'rows, ' + str(self.m) + 'columns.')

if __name__ == '__main__':
    for i in range(100):
        print(Fibonacci(i))