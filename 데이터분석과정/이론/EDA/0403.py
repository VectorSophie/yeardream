import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from elice_utils import elice_utils

def make_boxplot(data: pd.DataFrame):

    plt.figure(figsize=(7,5)) 
    sns.boxplot(data=data, x="year", y="passengers")  
    show_plot("boxplot")  


def show_plot(fig_name: str):

    plt.savefig(fig_name + ".png")
    elice_utils.send_image(fig_name + ".png")
    plt.cla()

def main():

    data = sns.load_dataset("flights")

    make_boxplot(data)

if __name__ == "__main__":
    main()
