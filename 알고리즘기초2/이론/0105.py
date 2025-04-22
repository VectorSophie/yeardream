import sys
N,M,K = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
prefix = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = arr[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

for _ in range(K):
    total = 0
    a,b,c,d = map(int,sys.stdin.readline().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    total = prefix[c + 1][d + 1] - prefix[a][d + 1] - prefix[c + 1][b] + prefix[a][b]
    print(total)

    