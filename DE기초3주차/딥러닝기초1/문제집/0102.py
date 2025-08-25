import numpy as np

from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron

from elice_utils import EliceUtils
elice_utils = EliceUtils()

np.random.seed(100)

def load_data():
    
    iris = load_iris()
    
    X = iris.data[:,2:4]
    Y = iris.target
    
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)
    
    return X_train, X_test, Y_train, Y_test

def main():   
    
    X_train, X_test, Y_train, Y_test = load_data()
    
    perceptron = Perceptron(max_iter=1000, eta0=0.0001)
    
    perceptron.fit(X_train,Y_train)
    
    pred = perceptron.predict(X_test)
    
    accuracy = accuracy_score(Y_test,pred)
    
    print("Test 데이터에 대한 정확도 : %0.5f" % accuracy)
    
    return X_train, X_test, Y_train, Y_test, pred

if __name__ == "__main__":
    main()