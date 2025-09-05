import matplotlib.pyplot as plt

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
 
from sklearn.datasets import load_boston

def load_data():
    
    X, y  = load_boston(return_X_y=True)
     
    print("데이터의 입력값(X)의 개수 :", X.shape[1])
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=100)
    
    return train_X, test_X, train_y, test_y

def Multi_Regression(train_X,train_y):
    
    multilinear = LinearRegression()
    
    multilinear.fit(train_X, train_y)
    
    return multilinear
    
def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    multilinear = Multi_Regression(train_X,train_y)
    
    predicted = multilinear.predict(test_X)
    
    model_score = multilinear.score(test_X, test_y)
    
    print("\n> 모델 평가 점수 :", model_score)
     
    beta_0 = multilinear.intercept_
    beta_i_list = multilinear.coef_
    
    print("\n> beta_0 : ",beta_0)
    print("> beta_i_list : ",beta_i_list)
    
    return predicted, beta_0, beta_i_list, model_score
    
if __name__ == "__main__":
    main()