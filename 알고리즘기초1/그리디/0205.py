N, M = map(int, input().split())  
A = list(map(int, input().split()))  

count = 0  
start = 0  
current_sum = 0  

for end in range(N):
    current_sum += A[end]  
    while current_sum > M and start <= end:  
        current_sum -= A[start]
        start += 1
    if current_sum == M: 
        count += 1

print(count)