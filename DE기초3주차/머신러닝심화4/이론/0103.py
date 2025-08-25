import pandas as pd

import warnings
warnings.filterwarnings(action='ignore')

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_data():
    
    X, y = load_breast_cancer(return_X_y = True)
    
    train_X, test_X, train_y ,test_y = train_test_split(X, y, test_size = 0.2, random_state = 156)
    
    return train_X, test_X, train_y ,test_y

def Voting_Clf(train_X, test_X, train_y ,test_y):
    
    lr_clf = LogisticRegression()
    knn_clf = KNeighborsClassifier()
    
    vo_clf = VotingClassifier(estimators = [('lr', lr_clf), ('knn', knn_clf)], voting = 'soft')
    
    vo_clf.fit(train_X, train_y)
    
    pred = vo_clf.predict(test_X)
    
    return lr_clf, knn_clf, vo_clf, pred
 
def main():
    
    train_X, test_X, train_y ,test_y = load_data()
    
    lr_clf, knn_clf,vo_clf, pred = Voting_Clf(train_X, test_X, train_y ,test_y)
    
    print('> Voting Classifier 정확도 : {0:.4f}\n'.format(accuracy_score(test_y, pred)))

    classifiers = [lr_clf, knn_clf]
    for classifier in classifiers:
        classifier.fit(train_X, train_y)
        pred = classifier.predict(test_X)
        class_name = classifier.__class__.__name__
        print("> {0} 정확도 : {1:.4f}".format(class_name, accuracy_score(test_y, pred)))

if __name__ =="__main__":
    main()