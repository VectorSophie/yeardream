from elice_utils import EliceUtils
import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
elice_utils = EliceUtils() 

[M, n, N] = [30, 5, 10]
stat_hyp = sp.stats.hypergeom(M, n, N)

fig, ax = plt.subplots()

x_axis = np.arange(n + 1)
plt.bar(x_axis, stat_hyp.pmf(x_axis))

plt.show()
fig.savefig("pmf_plot.png")
elice_utils.send_image("pmf_plot.png")

x_axis = np.arange(n + 1)
plt.bar(x_axis, stat_hyp.cdf(x_axis))

plt.show()
fig.savefig("cdf_plot.png")
elice_utils.send_image("cdf_plot.png")

np.random.seed(seed=0)

random_hyp = np.random.hypergeometric(ngood=5, nbad=25, nsample=10, size=50) 
print(random_hyp)

hyp_mean = np.mean(random_hyp)
print(hyp_mean)
