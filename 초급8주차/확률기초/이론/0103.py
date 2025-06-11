from itertools import permutations 
from itertools import combinations

rank_com = list(combinations(["가", "나", "다", "라", "마", "바"], 2))
rank_com_num = len(rank_com)

print(rank_com)
print(rank_com_num)