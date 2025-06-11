import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from elice_utils import EliceUtils 
elice_utils = EliceUtils()

drink_cup = pd.DataFrame({
    "cup": [22, 7, 19, 3, 10, 8, 19, 7, 15, 9, 35, 5], 
    "who": ["A", "E", "D", "B", "C", "A", "A", "A", "D", "B", "C", "B"],
    "stems": [2, 0, 1, 0, 1, 0, 1, 0, 1, 0, 3, 0]
})

print(drink_cup)

fig, ax = plt.subplots()

plt.hist(drink_cup["cup"])

plt.show()
fig.savefig("hist_plot.png")
elice_utils.send_image("hist_plot.png")