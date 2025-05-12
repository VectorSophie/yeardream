from elice_utils import EliceUtils
import matplotlib.pyplot as plt
elice_utils = EliceUtils()    

labels = ["A", "B", "C", "D", "E"]
ratio = [33,25,17,17,8]

fig, ax = plt.subplots()

plt.bar(labels, ratio)

plt.show()
fig.savefig("bar_plot.png")
elice_utils.send_image("bar_plot.png")