from statistics import variance, stdev
import numpy as np

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

cf_std = stdev(coffee)
print("Sample std.Dev : ", round(cf_std, 2))