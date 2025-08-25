import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def load_data():
    
    iris = load_iris()
    
    irisDF = pd.DataFrame(data = iris.data, columns = iris.feature_names)
    
    irisDF['target'] = iris.target
    
    return irisDF

def k_means_clus(irisDF):
    
    kmeans = KMeans(init='random', n_clusters=3, random_state=100)
    
    X = load_data()
    kmeans.fit(X)
    
    irisDF['cluster'] = kmeans.labels_

    iris_result = irisDF.groupby(['target','cluster'])['sepal length (cm)'].count()
    print(iris_result)
    
    return iris_result, irisDF

def Visualize(irisDF):
    
    pca = PCA(n_components=2)
    pca_transformed = pca.fit_transform(irisDF)

    irisDF['pca_x'] = pca_transformed[:,0]
    irisDF['pca_y'] = pca_transformed[:,1]

    idx_0 = irisDF[irisDF['cluster'] == 0].index
    idx_1 = irisDF[irisDF['cluster'] == 1].index
    idx_2 = irisDF[irisDF['cluster'] == 2].index
    
    fig, ax = plt.subplots()
    
    ax.scatter(x=irisDF.loc[idx_0, 'pca_x'], y= irisDF.loc[idx_0, 'pca_y'], marker = 'o')
    ax.scatter(x=irisDF.loc[idx_1, 'pca_x'], y= irisDF.loc[idx_1, 'pca_y'], marker = 's')
    ax.scatter(x=irisDF.loc[idx_2, 'pca_x'], y= irisDF.loc[idx_2, 'pca_y'], marker = '^')
    ax.set_title('K-menas')
    ax.set_xlabel('PCA1')
    ax.set_ylabel('PCA2')
    
    fig.savefig("plot.png")
    elice_utils.send_image("plot.png")


def main():
    
    irisDF = load_data()
    
    iris_result, irisDF = k_means_clus(irisDF)
    
    Visualize(irisDF)
    
if __name__ == "__main__":
    main()
