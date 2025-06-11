import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.datasets import make_blobs

from elice_utils import EliceUtils
elice_utils = EliceUtils()

X, y = make_blobs(n_samples=300, n_features=2, centers=3, cluster_std=0.8, random_state=0)

transformation = [[0.60834549, -0.63667341],[-0.40887718,0.85253229]]
X_aniso = np.dot(X, transformation)

clusterDF = pd.DataFrame(data = X_aniso, columns= ['ftr1','ftr2'])
clusterDF['target'] = y
target_list = np.unique(y)

def data_visualize():
    fig, ax = plt.subplots()
    plt.title('data')
    
    for target in target_list:
        target_cluster = clusterDF[clusterDF['target'] == target]
        ax.scatter(x = target_cluster['ftr1'], y = target_cluster['ftr2'])
    
    fig.savefig("plot.png")
    elice_utils.send_image("plot.png")

def K_means():
    
    k_means = KMeans(init='random', n_clusters=3, random_state=0)
    
    kmeans_label = k_means.fit_predict(X_aniso)
    
    clusterDF['kmeans_label']=kmeans_label

    center = k_means.cluster_centers_

    unique_labels = np.unique(kmeans_label)
    fig, ax = plt.subplots()
    plt.title('K-Means')
    
    for label in unique_labels:
        label_cluster = clusterDF[clusterDF['kmeans_label'] == label]
        center_x_y = center[label]
        ax.scatter(x = label_cluster['ftr1'], y = label_cluster['ftr2'])
        ax.scatter(x = center_x_y[0], y = center_x_y[1], s = 70,color = 'k', marker = '$%d$' % label)
    
    fig.savefig("plot.png")
    elice_utils.send_image("plot.png")

    print("K-means Clustering")
    print(clusterDF.groupby('target')['kmeans_label'].value_counts())
    
    return kmeans_label

def GMM():
    
    gmm = GaussianMixture(n_components=3, random_state=0)
    
    gmm_label = gmm.fit(X_aniso).predict(X_aniso)
    
    clusterDF['gmm_label']=gmm_label
    
    unique_labels = np.unique(gmm_label)

    fig, ax = plt.subplots()
    plt.title('GMM')
    
    for label in unique_labels:
        label_cluster = clusterDF[clusterDF['gmm_label'] == label]
        plt.scatter(x = label_cluster['ftr1'], y = label_cluster['ftr2'])
    
    fig.savefig("plot.png")
    elice_utils.send_image("plot.png")
    
    print("Gaussian Mixture Model")
    print(clusterDF.groupby('target')['gmm_label'].value_counts())
    
    return gmm_label

def main():
    data_visualize()
    K_means()
    GMM()

if __name__ == "__main__":
    main()
