from statistics import variance, stdev
import numpy as np

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

cf_quant_20 = np.percentile(coffee, 20)
cf_quant_80 = np.percentile(coffee, 80)
print("20 Quantiles : ", cf_quant_20)
print("80 Quantiles : ", cf_quant_80)