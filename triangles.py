def triangles(s: int =10):
    L = [1]
    n=0
    while n<s:
        yield L # 第一次返回[1]
        L.append(0) # L = [1, 0]
        L = [L[i-1]+L[i] for i in range(len(L))] # [ L[-1] + L[1], L[0] + L[1] ] = [1, 1]
        n=n+1
        pass

for i in triangles():
    print(i)