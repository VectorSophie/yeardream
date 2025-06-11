import numpy as np
from scipy import stats

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

cf_mean = np.mean(coffee)
print("Mean :", round(cf_mean, 2))