N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
print(A[0]*A[1])