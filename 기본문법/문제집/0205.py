a,b,c,d = map(int, input().split())

if ((a<=b and a==d and b>c and c<6) or (a==b and a==c and a==d)):
    print("True")
else:
    print("False")