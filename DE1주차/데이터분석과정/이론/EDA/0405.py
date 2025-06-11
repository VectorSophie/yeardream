import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from elice_utils import elice_utils

def year_plot(data: pd.DataFrame):

    sns.barplot(data=data,x="year",y="passengers",palette="rocket",ci=None)
    show_plot("year_plot")

def month_plot(data: pd.DataFrame):

    sns.barplot(data=data,x="month",y="passengers",palette="rocket",ci=None)
    show_plot("month_plot")

def show_plot(fig_name: str):

    plt.savefig(fig_name + ".png")
    elice_utils.send_image(fig_name + ".png")
    plt.cla()

def main():

    data = sns.load_dataset("flights")

    year_plot(data)

    month_plot(data)

if __name__ == "__main__":
    main()
