from itertools import product
from itertools import combinations_with_replacement

re_per = list(product(["A", "B", "C", "D", "E"], repeat=3))
re_per_num = len(re_per)

print(re_per)
print(re_per_num)