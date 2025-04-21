import math

T = int(input())

for _ in range(T):
    n = int(input())
    if int(math.sqrt(n))**2 == n:
        print("Odd")
    else:
        print("Even")
