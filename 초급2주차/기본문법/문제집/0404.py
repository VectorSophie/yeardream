n = int(input())
m = 0

for i in range(1,n+1):
    if n % i == 0:
        if m % 10 == 0:
            print(end = "\n")
        print(i, end = " ")
        m += 1