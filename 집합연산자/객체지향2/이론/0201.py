import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

temperatures = [
    22.8, 25.3, 32.6, 31.8, 29.0, 27.1, 29.2,
    28.1, 24.2, 26.5, 29.5, 28.2, 30.9, 31.9,
    33.2, 34.0, 32.1, 33.2, 34.1, 34.7, 36.9,
    38.0, 35.7, 36.8, 34.1, 33.7, 35.4, 35.2,
    36.7, 36.9, 38.3
]

x = [i for i in range(len(temperatures))]

plt.bar(x, temperatures)

plt.savefig('graph.png')
elice_utils.send_image('graph.png')