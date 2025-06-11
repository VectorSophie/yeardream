import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

from elice_utils import elice_utils

def make_scatter(df: pd.DataFrame):

    plt.scatter(x=df["bmi"],y=df["target"],alpha=0.5)
    show_plot("scatter") 

def make_heatmap(df: pd.DataFrame):

    corr = df.corr()
    sns.heatmap(corr)
    show_plot("heatmap")  


def show_plot(fig_name: str):

    plt.savefig(fig_name + ".png")
    elice_utils.send_image(fig_name + ".png")
    plt.cla()

def main():

    data = datasets.load_diabetes()
    df = pd.DataFrame(data["data"], columns=data["feature_names"])
    df["target"] = data["target"]

    print(df.head())

    make_scatter(df)

    make_heatmap(df)

if __name__ == "__main__":
    main()
