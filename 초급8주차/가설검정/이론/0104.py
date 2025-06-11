from elice_utils import EliceUtils
import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy import stats
elice_utils = EliceUtils() 

stat_nor = sp.stats.norm(0,1)

fig, ax = plt.subplots()

x_axis = np.linspace(-3, 3, 100)
plt.bar(x_axis, stat_nor.pdf(x_axis))

plt.show()
fig.savefig("pdf_plot.png")
elice_utils.send_image("pdf_plot.png")

x_axis = np.linspace(-3, 3, 100)
plt.bar(x_axis, stat_nor.cdf(x_axis))

plt.show()
fig.savefig("cdf_plot.png")
elice_utils.send_image("cdf_plot.png")

np.random.seed(seed=0)

random_nor = np.random.normal(0, 1, 100)
print(random_nor) 

nor_mean = np.mean(random_nor)
print(nor_mean)