def dfs(n):
    for i in v[n]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

n, m = map(int,input().split())
visited = [False] * 201
cnt = 0
v = [[] for _ in range(201)]

for _ in range(m):
    a, b = map(int,input().split())
    v[a].append(b)
    v[b].append(a)

for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        cnt += 1
print(cnt)