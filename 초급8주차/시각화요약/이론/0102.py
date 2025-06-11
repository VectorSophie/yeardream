import pandas as pd 
import numpy as np

drink = pd.read_csv("drink.csv")

drink_relfreq = drink[drink["Attend"] == 1]["Name"].value_counts(normalize=True)

print("상대도수 계산")
print(drink_relfreq)