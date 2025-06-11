import numpy as np 
import pandas as pd
import matplotlib as plt

mart = pd.read_csv("mart.csv")
print(mart)

region_crosstab = pd.crosstab(mart["region"], mart["mart"])
print(region_crosstab)

famnum_crosstab = pd.crosstab(mart["family_num"], mart["mart"])
print(famnum_crosstab)