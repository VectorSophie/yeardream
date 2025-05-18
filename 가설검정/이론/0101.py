from elice_utils import EliceUtils
import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
elice_utils = EliceUtils()    

n, p = 10, 0.3
stat_bin = sp.stats.binom(n, p)

fig, ax = plt.subplots()

x_axis = np.arange(n + 1) 
plt.bar(x_axis, stat_bin.pmf(x_axis))

##
plt.show()
fig.savefig("pmf_plot.png")
elice_utils.send_image("pmf_plot.png")

x_axis = np.arange(n + 1) 
plt.bar(x_axis, stat_bin.cdf(x_axis))

plt.show()
fig.savefig("cdf_plot.png")
elice_utils.send_image("cdf_plot.png")

np.random.seed(seed=0)

random_bin = np.random.binomial(n=10, p=0.3, size=50)
print(random_bin)

bin_mean = np.mean(random_bin)
print(bin_mean)