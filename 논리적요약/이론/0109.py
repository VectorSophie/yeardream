from statistics import variance, stdev
import numpy as np

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

cf_cv = stdev(coffee) / np.mean(coffee)
cf_cv = round(cf_cv, 2)
print("CV:", cf_cv)