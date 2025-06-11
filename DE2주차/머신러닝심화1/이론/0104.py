from elice_utils import EliceUtils
elice_utils = EliceUtils()

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import PolynomialFeatures

def load_data():
    
    np.random.seed(0)
    
    X = 3*np.random.rand(50, 1) + 1
    y = X**2 + X + 2 +5*np.random.rand(50,1)
    
    return X, y

def Polynomial_transform(X):
    
    poly_feat = PolynomialFeatures(degree=2, include_bias=True)
    
    poly_X = poly_feat.fit_transform(X)
    
    print("변환 이후 X 데이터\n",poly_X[:3])
    
    return poly_X

def Multi_Regression(poly_x, y):
    
    multilinear = LinearRegression().fit(poly_x,y)
    
    return multilinear

def plotting_graph(x,y,predicted):
    fig = plt.figure()
    plt.scatter(x, y)
    
    plt.scatter(x, predicted,c='r')
    plt.savefig("test.png")
    elice_utils.send_image("test.png")
    
def main():
    
    X,y = load_data()
    
    poly_x = Polynomial_transform(X)
    
    linear_model = Multi_Regression(poly_x,y)
    
    predicted = linear_model.predict(poly_x)
    
    plotting_graph(X,y,predicted)
    
    return predicted
    
if __name__=="__main__":
    main()