from statistics import variance, stdev
import numpy as np

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

cf_range = np.max(coffee, axis=0) - np.min(coffee, axis=0)
print("Range :", cf_range)
