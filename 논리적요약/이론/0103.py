import numpy as np
from scipy import stats

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

cf_mode = stats.mode(coffee)
print("Mode :", cf_mode[0][0])