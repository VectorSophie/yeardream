import matplotlib.pyplot as plt
import numpy as np
from elice_utils import elice_utils

def make_plots(data: np.ndarray):

    plt.plot(data,data**2,"gs",data,data**3,"ro")
    show_plot("plot")  

def show_plot(fig_name: str):

    plt.savefig(fig_name + ".png")
    elice_utils.send_image(fig_name + ".png")
    plt.cla()


def main():

    time = np.arange(0, 10, 0.5)

    make_plots(time)

if __name__ == "__main__":
    main()
