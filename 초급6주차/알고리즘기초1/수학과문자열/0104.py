n = int(input())
is_prime = [True] * (n + 1)
is_prime[0:2] = [False, False] 

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

prime_count = sum(is_prime)
print(prime_count)