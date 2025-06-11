import pandas as pd 
import numpy as np

drink = pd.read_csv("drink.csv")

drink_freq = drink[drink["Attend"] == 1]["Name"].value_counts()

print("도수 계산")
print(drink_freq)