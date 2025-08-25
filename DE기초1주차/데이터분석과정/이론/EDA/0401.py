import matplotlib.pyplot as plt
import numpy as np
from elice_utils import elice_utils

def make_plot(data: np.ndarray):

    plt.plot(data, data**2, "b--")
    show_plot("plot")  # 삭제 금지

def show_plot(fig_name: str):

    plt.savefig(fig_name + ".png")
    elice_utils.send_image(fig_name + ".png")
    plt.cla()

def main():

    time = np.arange(0, 10, 0.5)

    make_plot(time)

if __name__ == "__main__":
    main()