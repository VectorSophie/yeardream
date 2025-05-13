from elice_utils import EliceUtils
import numpy as np
import matplotlib.pyplot as plt
elice_utils = EliceUtils()  

coffee = np.array([202, 177, 121, 148, 89, 121, 137, 158])

fig, ax = plt.subplots()

plt.boxplot(coffee)

plt.show()
fig.savefig("box_plot.png")
elice_utils.send_image("box_plot.png")