import math
import sys

def is_palindrome(s):
    return s == s[::-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    s = sys.stdin.readline().strip()
    num = int(s)
    if is_palindrome(s) and is_prime(num):
        cnt += 1
print(cnt)
