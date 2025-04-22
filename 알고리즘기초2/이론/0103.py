def ration(N):
    for i in range(N // 5, -1, -1): 
        remain = N - (i * 5)
        if remain % 3 == 0:
            return i + (remain // 3)
    return -1  

N = int(input())
print(ration(N))