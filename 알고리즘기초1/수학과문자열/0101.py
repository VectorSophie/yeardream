T = int(input())
for i in range(T):
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        if N % i == 0:
            cnt += 1
    if cnt % 2 == 0:
        print("Even")
    else:
        print("Odd")
