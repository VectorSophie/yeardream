n = int(input())

fib = [0,1]
if n == 1:
    print([0])
else:
    fib = [0, 1]
    while fib[-1] + fib[-2] < n:
        fib.append(fib[-1] + fib[-2])
    print(fib)