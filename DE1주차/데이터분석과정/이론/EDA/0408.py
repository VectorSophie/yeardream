import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from elice_utils import elice_utils

def make_hist(data: np.ndarray, name: str):

    plt.hist(data,bins=40)
    show_plot(name)  

def std_scale(data: np.ndarray) -> np.ndarray:

    std = StandardScaler()
    std.fit(data)
    scaled = std.transform(data)
    return scaled

def show_plot(fig_name: str):

    plt.savefig(fig_name + ".png")
    elice_utils.send_image(fig_name + ".png")
    plt.cla()

def main():

    dataset = datasets.load_breast_cancer()
    data = dataset.data

    make_hist(data.flatten(), "before")

    scaled = std_scale(data)
    make_hist(scaled.flatten(), "scaled")

if __name__ == "__main__":
    main()
