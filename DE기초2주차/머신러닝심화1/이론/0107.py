import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from elice_utils import EliceUtils
elice_utils = EliceUtils()

from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston

def load_data():
    
    X, y = load_boston(return_X_y = True)
    
    feature_names = load_boston().feature_names
    
    return X,y,feature_names

def ElasticNet_regression(train_X, train_y):
    
    ElasticNet_reg = ElasticNet(alpha=0.001,l1_ratio=0.05)
    ElasticNet_reg.fit(train_X,train_y)
    
    return ElasticNet_reg
  
def plot_graph(coef):
    coef.plot(kind='bar')
    
    plt.savefig("result.png")
    elice_utils.send_image("result.png")
    
def main():
    
    X,y,feature_names = load_data()
    
    train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.2, random_state=100)
    
    elasticnet_reg = ElasticNet_regression(train_X, train_y)

    score = elasticnet_reg.score(test_X,test_y)
    print("ElasticNet 회귀의 평가 점수:", score)
    
    ElasticNet_coef = pd.Series(elasticnet_reg.coef_, feature_names).sort_values()
    print("\nElasticNet 회귀의 beta_i\n", ElasticNet_coef)
    
    plot_graph(ElasticNet_coef)
    
    return elasticnet_reg

if __name__=="__main__":
    main()