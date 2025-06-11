import numpy as np
import pandas as pd

drink_cup = pd.DataFrame({
    "cup": [22, 7, 19, 3, 10, 8, 19, 7, 15, 9, 35, 5], 
    "who": ["A", "E", "D", "B", "C", "A", "A", "A", "D", "B", "C", "B"]
})

print(drink_cup)

factor_cup = pd.cut(drink_cup.cup, 4)
group_cup = drink_cup["cup"].groupby(factor_cup)
count_cup = group_cup.agg(["count"])

print(count_cup)