# 冒泡排序

lyst = [1, 4, 5, 5, 2, 3]

def swap(lyst, i, j):
    lyst[i], lyst[j] = lyst[j], lyst[i]

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        swaped = False
        while i < n:
            if lyst[i] > lyst[i-1]:
                swap(lyst, i, i-1)
                swaped = True
            i +=1
        if not swaped: return
        n -=1

bubbleSort(lyst)
print(lyst)