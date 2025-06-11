import numpy as np 
import scipy as sp
from scipy import stats

np.random.seed(seed = 0)

random_nor = np.random.normal(100,5,10)
print(random_nor)

nor_mean = np.mean(random_nor)
print(nor_mean)

def ztest(stat, mu, sigma):
    z = (stat.mean() - mu) / (sigma / np.sqrt(len(stat)))
    return (2 * (1 - sp.stats.norm.cdf(z)))

mu_test = ztest(random_nor, 100, 5) 
print(mu_test)