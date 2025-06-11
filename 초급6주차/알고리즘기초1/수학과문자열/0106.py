def VPS(p):
    arr = []
    for checker in p:
        if checker == '(':
            arr.append(checker)
        else:
            if len(arr) == 0:
                return "NO"
            arr.pop()
    if len(arr) == 0:
        return "YES"
    else:
         return "NO"
S = input()
print(VPS(S))
