from itertools import product
from itertools import combinations_with_replacement

re_com = list(combinations_with_replacement(["A", "B", "C", "D", "E"], 3))
re_com_num = len(re_com)

print(re_com)
print(re_com_num)
