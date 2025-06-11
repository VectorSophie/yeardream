from elice_utils import EliceUtils
elice_utils = EliceUtils()

import numpy as np
from sklearn.decomposition import PCA
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

def load_data():
    
    X, y = load_wine(return_X_y=True)
    
    column_start = 6
    X = X[:, column_start : column_start+2]
    print(X.shape)
    return X

def pca_data(X):
    
    pca = PCA(n_components=1)
    
    pca.fit(X)
    
    X_pca = pca.transform(X)
    
    return pca, X_pca

def visualize(pca, X, X_pca):
    X_new = pca.inverse_transform(X_pca)
    
    plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
    plt.scatter(X_new[:, 0], X_new[:, 1], alpha=0.8)
    plt.axis('equal');
    
    plt.savefig('PCA.png')
    elice_utils.send_image('PCA.png')

def main():
    
    X = load_data()
    
    pca, X_pca = pca_data(X)
    
    print("- original shape:   ", X.shape)
    print("- transformed shape:", X_pca.shape)
    
    visualize(pca, X, X_pca)
    
if __name__ == '__main__':
    main()