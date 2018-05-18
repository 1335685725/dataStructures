# 对于外层循环， 总是执行n-1次， 当第一次通过外层循环时， 内层循环执行n-1次， 第二次时，内层循环n-2次，
# 所以 一共执行了 (n-1)+(n-2)+(n-3)+(n-4)+..+1 = n(n-1)/2= (1/2)n²-(1/2)n，对于较大的N，我们选择影响最大的项，忽略常数系数
# 所以选择排序在各种情况下的复杂度为O(n²)



lyst = [3, 5, 1, 2, 5, 6]


def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]

def selectionSort(lyst):
    i = 0
    while i < len(lyst)-1:
        max_index = i
        j = i + 1
        while j <len(lyst):
            if lyst[max_index] < lyst[j]:
                max_index = j
            j+=1
        if max_index != i:
            swap(lyst, max_index, i)
        i+=1
    return lyst
print(selectionSort(lyst))