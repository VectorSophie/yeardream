from elice_utils import EliceUtils
elice_utils = EliceUtils()

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score

def load_data():
    
    np.random.seed(0)
    
    X = 5*np.random.rand(100,1)
    y = 3*X + 5*np.random.rand(100,1)
    
    train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.3, random_state=0)
    
    return train_X, train_y, test_X, test_y

def Linear_Regression(train_X, train_y):
    
    lr = LinearRegression()
    
    lr.fit(train_X,train_y)
    
    return lr

def plotting_graph(test_X, test_y, predicted):
    plt.scatter(test_X,test_y)
    plt.plot(test_X, predicted, color='r')
    
    plt.savefig("result.png")
    elice_utils.send_image("result.png")

"""
1. 정의한 함수들을 이용하여 main() 함수를 완성합니다.
"""
def main():
    
    train_X, train_y, test_X, test_y = load_data()
    
    lr = Linear_Regression(train_X, train_y)
   
    predicted = lr.predict(test_X)

    R_squared = lr.score(test_X, test_y)
    
    print("> R_squared :",R_squared)
    
    plotting_graph(test_X, test_y, predicted)
    
    return R_squared

if __name__=="__main__":
    main()