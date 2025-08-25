import numpy as np
import matplotlib.pyplot as plt
import csv

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def main():
    
    data_x = []
    data_y = []
    
    with open('./data/data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data_x.append(float(row[0]))
            data_y.append(float(row[1]))

    fig, axes = plt.subplots(2,2)

    colors = np.random.randint(0,100,500)
 
    axes[0,0].scatter(data_x,data_y,c=colors,s=2,alpha=0.7)
   
    bar_x = np.arange(10)

    axes[0,1].bar(bar_x, bar_x**2)

    x = np.array([3,2,1])
    y = np.array([2,3,2])
    z = np.array([1,3,4])
    data1 =  [x, y, z]

    x_ax =  np.arange(3)
    
    for i in x_ax:

        axes[1,0].bar(x_ax, data1[i], bottom=np.sum(data1[:i], axis=0))

    axes[1,0].set_xticks(x_ax)

    axes[1,0].set_xticklabels(['A','B','C'])
    
    data = np.array(data_x)

    axes[1,1].hist(data,bins=50)

    fig.savefig("plot.png")
    elice_utils.send_image("plot.png")

if __name__ == '__main__':
    main()