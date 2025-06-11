N = int(input())
A = list(map(int,input().split()))
maax = 0
for i in range(N):
    for j in range(i+1,N):
        maax = max(maax, A[i]*A[j])
print(maax)