import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from elice_utils import EliceUtils
elice_utils = EliceUtils()

from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

from sklearn.datasets import load_boston

def load_data():
    
    X, y = load_boston(return_X_y = True)
    
    feature_names = load_boston().feature_names
    
    return X,y,feature_names
    
def Ridge_regression(X, y):
    
    ridge_reg = Ridge(alpha=10)
    
    ridge_reg.fit(X, y)
    
    return ridge_reg

def Lasso_regression(X, y):
    
    lasso_reg = Lasso(alpha=10)
    
    lasso_reg.fit(X, y)
    
    return lasso_reg
    
def plot_graph(coef, title):
    fig = plt.figure()
    
    plt.ylim(-1,1)
    plt.title(title)
    coef.plot(kind='bar')

    plt.savefig("result.png")
    elice_utils.send_image("result.png")


def main():
    
    X,y,feature_names = load_data()
    
    ridge_reg = Ridge_regression(X, y)
    lasso_reg = Lasso_regression(X, y)
    
    ridge_coef = pd.Series(ridge_reg.coef_, feature_names).sort_values()
    print("Ridge 회귀의 beta_i\n", ridge_coef)
    
    lasso_coef = pd.Series(lasso_reg.coef_, feature_names).sort_values()
    print("Lasso 회귀의 beta_i\n", lasso_coef)
    
    plot_graph(ridge_coef, 'Ridge')
    plot_graph(lasso_coef, 'Lasso')

if __name__=="__main__":
    main()