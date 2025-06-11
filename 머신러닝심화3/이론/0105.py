import numpy as np
from sklearn.manifold import TSNE
from sklearn.datasets import load_wine
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def load_data():
    
    X, y = load_wine(return_X_y=True)
    
    column_start = 6
    X = X[:, column_start : column_start+2]
    print(X.shape)
    return X

def tsne_data(X):
    
    tsne = TSNE(n_components=1)

    X_tsne = tsne.fit_transform(X)
    
    return tsne, X_tsne

def main():
    
    X = load_data()
    
    tsne, X_tsne = tsne_data(X)
    
    print("- original shape:   ", X.shape)
    print("- transformed shape:", X_tsne.shape)
    
    print("\n원본 데이터 X :\n", X[:5])
    print("\n차원 축소 이후 데이터 X_tsne\n",X_tsne[:5])
    
if __name__ == '__main__':
    main()