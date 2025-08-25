from data_plot import *
import warnings
warnings.filterwarnings(action='ignore')

import numpy as np
from sklearn.linear_model import LogisticRegression

from sklearn.model_selection import train_test_split

def load_data():
    
    np.random.seed(0)
    
    X = np.random.normal(size = 100)
    y = (X > 0).astype(np.float)
    X[X > 0] *= 5
    X += .7 * np.random.normal(size = 100)
    X = X[:, np.newaxis]
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 100)
    
    return train_X, test_X, train_y, test_y

def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    logistic_model = LogisticRegression()
    
    logistic_model.fit(train_X,train_y)
    
    predicted = logistic_model.predict(test_X)

    print("예측 결과 :", predicted[:10])
    
    plot_logistic_regression(logistic_model, train_X, train_y)
    
    return logistic_model

if __name__ == "__main__":
    main()
