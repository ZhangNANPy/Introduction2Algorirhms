# -*- coding: utf-8 -*-
'''
一个矩形区域被划分为N*M个小矩形格子，在格子(i,j)中有A[i][j]个苹果。
现在从左上角的格子(1,1)出发，要求每次只能向右走一步或向下走一步，最后到达(N,M)，
每经过一个格子就把其中的苹果全部拿走。请找出能拿到最多苹果数的路线。
'''
def applesMax(b):
    resM = [[0 for j in range(len(b[0]) + 1)] for i in range(len(b) + 1)]
    for i in range(1, len(b) + 1):
        for j in range(1, len(b[0]) + 1):
            resM[i][j] = max(resM[i - 1][j], resM[i][j - 1]) + b[i - 1][j - 1]
    return resM[len(b)][len(b[0])]

if __name__ == '__main__':
    print(applesMax([[1,2,3],[6,5,4],[8,7,9]]))