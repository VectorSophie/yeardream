import numpy as np
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

np.random.seed(0)

mean = 2
std = 1

n_samples = np.random.normal(mean, std, 1000)

count, bins, ignored = plt.hist(n_samples, 20, density=True)

plt.plot(bins, 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * std**2) ), linewidth=3, color='y')
plt.savefig("result.png")
elice_utils.send_image("result.png")

n_samples_m = np.mean(n_samples)
print("Samples mean: {}".format(n_samples_m))

n_samples_std = np.std(n_samples)
print("Samples std: {}".format(n_samples_std))