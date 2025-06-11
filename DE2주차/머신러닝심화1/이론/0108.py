import matplotlib.pyplot as plt
import numpy as np

from elice_utils import EliceUtils
elice_utils = EliceUtils()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

def return_RSS(test_y, predicted):
    
    RSS = 0
    for i in range(len(test_y)):
        RSS += (test_y[i] - predicted[i]) ** 2
    return RSS

def plotting_graph(test_X, test_y, predicted):
    plt.scatter(test_X,test_y)
    plt.plot(test_X, predicted, color='r')
    
    plt.savefig("result.png")
    elice_utils.send_image("result.png")

def main():
    
    train_X, train_y, test_X, test_y = load_data()
     
    lr = Linear_Regression(train_X, train_y)
    
    predicted = lr.predict(test_X)
    
    RSS = return_RSS(test_y, predicted)
    print("> RSS :",RSS)
    
    plotting_graph(test_X, test_y, predicted)

if __name__=="__main__":
    main()