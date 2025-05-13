from elice_utils import EliceUtils
import matplotlib.pyplot as plt
import pandas as pd
elice_utils = EliceUtils()

body = pd.read_csv("body.csv")

fig, ax = plt.subplots()

plt.scatter(body["height"], body["weight"])

plt.show()
fig.savefig("height_weight_plot.png")
elice_utils.send_image("height_weight_plot.png")

fig, ax = plt.subplots()

plt.scatter(body["height"], body["body_fat"])

plt.show()
fig.savefig("height_fat_plot.png")
elice_utils.send_image("height_fat_plot.png")

fig, ax = plt.subplots()

plt.scatter(body["height"], body["leglen"])

plt.show()
fig.savefig("height_leglen_plot.png")
elice_utils.send_image("height_leglen_plot.png")

fig, ax = plt.subplots()

plt.scatter(body["height"], body["hair"])

plt.show()
fig.savefig("height_hair_plot.png")
elice_utils.send_image("height_hair_plot.png")