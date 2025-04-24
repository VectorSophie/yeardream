from collections import deque

def OOB(x,y):
    return 1 <= x <= n and 1 <= y <= m

n, m = map(int,input().split())
board = [[0]* 101 for _ in range(101)]
visited = [[False]* 101 for _ in range(101)]

for i in range(1,n+1):
    row = list(map(int,input().split()))
    for j in range(1,m+1):
        board[i][j] = row[j-1]
q = deque()
q.append((1,1,0))
visited[1][1] = True

while q:
    x,y,cnt = q.popleft()
    if x == n and y == m:
        print(cnt)
        break
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if OOB(nx,ny) and not visited[nx][ny] and board[nx][ny]:
            q.append((nx,ny,cnt+1))
            visited[nx][ny] = True
else:
    print(-1)