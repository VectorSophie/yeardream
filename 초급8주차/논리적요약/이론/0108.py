from statistics import variance, stdev
import numpy as np

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

q75, q25 = np.percentile(coffee, [75, 25])
cf_IQR = q75 - q25
print("Inter quartile range:", cf_IQR)