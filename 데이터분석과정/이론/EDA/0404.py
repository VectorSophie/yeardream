import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from elice_utils import elice_utils

def make_scatter(data: pd.DataFrame):
   
    plt.figure(figsize=(5,5))  
    sns.scatterplot(data=data,x="total_bill",y="tip",hue="time")  
    show_plot("scatter")  


def show_plot(fig_name: str):

    plt.savefig(fig_name + ".png")
    elice_utils.send_image(fig_name + ".png")
    plt.cla()


def main():

    data = sns.load_dataset("tips")

    make_scatter(data)

if __name__ == "__main__":
    main()
