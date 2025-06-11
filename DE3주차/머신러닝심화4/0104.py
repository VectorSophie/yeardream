import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_data():
    X, y = load_breast_cancer(return_X_y = True)
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.2, random_state = 156)
    
    return train_X, test_X, train_y, test_y

def Bagging_Clf(train_X, test_X, train_y, test_y):
    
    ba_clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(),n_estimators=2)

    ba_clf.fit(train_X,train_y)
    
    pred = ba_clf.predict(test_X)
    
    return ba_clf, pred
    
def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    ba_clf, pred = Bagging_Clf(train_X, test_X, train_y, test_y)
    
    print('Bagging Classifier 정확도 : {0:.4f}'.format(accuracy_score(test_y, pred)))

    single_dt = DecisionTreeClassifier()
    single_dt.fit(train_X,train_y)
    single_pred = single_dt.predict(test_X)
    print('Single Decision Tree Classifier 정확도 : {0:.4f}'.format(accuracy_score(test_y, single_pred)))

if __name__ =="__main__":
    main()