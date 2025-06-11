from elice_utils import EliceUtils
import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
elice_utils = EliceUtils() 

stat_uni = sp.stats.uniform(0, 1)

fig, ax = plt.subplots()

x_axis = np.linspace(0, 1, 100)
plt.bar(x_axis, stat_uni.pdf(x_axis))

plt.show()
fig.savefig("pdf_plot.png")
elice_utils.send_image("pdf_plot.png")

x_axis = np.linspace(0, 1, 100)
plt.bar(x_axis, stat_uni.cdf(x_axis))

plt.show()
fig.savefig("cdf_plot.png")
elice_utils.send_image("cdf_plot.png")

np.random.seed(seed=0)

random_uni = np.random.uniform(0, 1, 100)
print(random_uni) 

uni_mean = np.mean(random_uni)
print(uni_mean)