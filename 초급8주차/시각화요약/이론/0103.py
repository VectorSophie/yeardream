import pandas as pd 
import numpy as np

drink = pd.read_csv("drink.csv")

drink_tab = pd.crosstab(index = drink["Attend"], columns = "count")

print("전체 참석 횟수를 확인하는 도수분포표")
print(drink_tab)

drink_who = pd.crosstab(index = drink["Attend"], columns = drink["Name"])

print("누가 몇 번 참석했는지 알 수 있는 도수분포표")
print(drink_who)