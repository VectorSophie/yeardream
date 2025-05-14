from itertools import permutations 
from itertools import combinations

rank_per = list(permutations(["가", "나", "다", "라", "마", "바"], 2))
rank_per_num = len(rank_per)

print(rank_per)
print(rank_per_num)