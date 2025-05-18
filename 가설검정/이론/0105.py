import numpy as np 
import scipy as sp
from scipy import stats

np.random.seed(seed = 0)

random_ber = np.random.binomial(n=1, p=0.5, size=50)
print(random_ber)

n_ber = np.count_nonzero(random_ber)
print(n_ber)

binom_test = sp.stats.binom_test(n_ber, 50)
print(binom_test)