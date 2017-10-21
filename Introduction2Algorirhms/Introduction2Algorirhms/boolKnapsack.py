# -*- coding: utf-8 -*-
def boolKnapsack(weight, value, capacity):
    if len(weight) != len(value):
        return 'Some items do not have weight or value!'
    resMatrix = [[0 for i in range(len(weight) + 1)] for j in range(capacity + 1)]
    for i in range(1, capacity + 1):#注意这里i、j是行列号，j指示第几个物品，i说名当前背包容量
        for j in range(1, len(weight) + 1):
            if i < weight[j - 1]:
                resMatrix[i][j] = resMatrix[i][j - 1]
            else:
                resMatrix[i][j] = max(resMatrix[i][j - 1], resMatrix[i - weight[j - 1]][j -1] + value[j - 1])
    return resMatrix[capacity][len(weight)]

if __name__ == '__main__':
    print(boolKnapsack([1,2,3], [3,5,6], 5))