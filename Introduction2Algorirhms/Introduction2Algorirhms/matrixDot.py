# -*- coding: utf-8 -*-
def matrixDot(x,y):
    maxColumn = 0
    for row in x:
        if len(row) > maxColumn:
            maxColumn = len(row)
    if maxColumn != len(y):
        raise MatrixLengthError(len(y), maxColumn)
    for row in x:
        while len(row) < maxColumn:
            row.append(0)
    maxColumn = 0
    for row in y:
        if len(row) > maxColumn:
            maxColumn = len(row)
    for row in y:
        while len(row) < maxColumn:
            row.append(0)
    res = [[0 for j in range(len(y[0]))] for i in range(len(x))]
    for row in range(len(res)):
            for column in range(len(res[0])):
                for k in range(len(x[0])):
                    res[row][column] += x[row][k] * y[k][column]
    return res


class MatrixLengthError(Exception):
    def __init__(self, row, column):
        self.column = column
        self.row = row
    def __str__(self):
        return repr('The number of matrix columns is not equal to the number of rows!\n' + str(self.row) + 'rows, ' + str(self.column) + 'columns.')

if __name__ == '__main__':
    print(matrixDot([[1, 1], [1, 1]], [[1, 1], [1, 1]]))