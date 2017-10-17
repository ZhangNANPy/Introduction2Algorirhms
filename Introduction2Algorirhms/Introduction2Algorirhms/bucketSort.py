# -*- coding: utf-8 -*-
def bucketSort(l):
    '''
    桶排序
    元素进桶的同时进行了插排
    '''
    sortMax = max(l) + 1
    n = len(l)#桶个数为n，或者sqrt(n)算法都会有线性时间复杂度
    temp  = [[] for i in range(n)]
    for i in l:
        k = int(n * (i / sortMax))#计算放在哪个桶中
        subList = temp[k]
        if subList == []:
            subList.append(i)
        else:
            subListLen = len(subList)
            flag = True
            for j in range(subListLen):
                if i <= subList[j]:
                    subList.insert(j, i)
                    flag = False
                    break
            if flag:
                subList.append(i)
    return [i for j in temp  if j != [] for i in j]

if __name__ == '__main__':
    a = [1,5,3,7,6,9,0,2,3,6,4]
    print(sorted(a))
    print(bucketSort(a))