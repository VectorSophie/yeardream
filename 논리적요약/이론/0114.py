from statistics import variance, stdev
import numpy as np 
import pandas as pd

body = pd.read_csv("body.csv")

cov_body = body.cov()

print(cov_body)