from statistics import variance, stdev
import numpy as np 
import pandas as pd

body = pd.read_csv("body.csv")

corr_body = body.corr()

print(corr_body)