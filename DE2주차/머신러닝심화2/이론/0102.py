import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

import warnings
warnings.filterwarnings(action='ignore')

from sklearn.model_selection import train_test_split  
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix 

def load_data():
    
    data = pd.read_csv('data/dataset.csv')
    
    X = data.drop('Class', axis=1)
    y = data['Class']
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 0)
    print(X, y)
    return train_X, test_X, train_y, test_y

def SVM(train_X, test_X, train_y, test_y):
    
    svm = SVC()
    
    svm.fit(train_X,train_y)
    
    pred_y = svm.predict(test_X)
    
    return pred_y

def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    pred_y = SVM(train_X, test_X, train_y, test_y)
    
    print("\nConfusion matrix : \n",confusion_matrix(test_y,pred_y))  
    print("\nReport : \n",classification_report(test_y,pred_y)) 

if __name__ == "__main__":
    main()
