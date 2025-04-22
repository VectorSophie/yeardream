N, M = map(int, input().split())  
A = list(map(int, input().split()))  

current_sum = sum(A[:M])
max_sum = current_sum

for i in range(1,N-M+1):
    current_sum = current_sum - A[i-1] + A[i+M-1]
    if current_sum > max_sum:
        max_sum = current_sum
print(max_sum)