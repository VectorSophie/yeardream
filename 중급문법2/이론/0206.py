import random

lotto = []

while len(lotto) != 6:
    a = random.randrange(1,45)
    if a in lotto:
        pass
    elif a not in lotto:
        lotto.append(a)
lotto.sort()
print(lotto)