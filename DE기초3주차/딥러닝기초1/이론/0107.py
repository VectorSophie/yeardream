import numpy as np
from visual import *
from sklearn.neural_network import MLPClassifier

from elice_utils import EliceUtils
elice_utils = EliceUtils()

import warnings
warnings.filterwarnings(action='ignore')

np.random.seed(100)
    
def read_data(filename):
    
    X = []
    Y = []
    
    with open(filename) as fp:
        N, M = fp.readline().split()
        N = int(N)
        M = int(M)
        
        for i in range(N):
            line = fp.readline().split()
            for j in range(M):
                X.append([i, j])
                Y.append(int(line[j]))
    
    X = np.array(X)
    Y = np.array(Y)
    
    return (X, Y)

def train_MLP_classifier(X, Y):
    
    clf = MLPClassifier(hidden_layer_sizes=(100,100))
    
    clf.fit(X,Y)
    
    return clf

def report_clf_stats(clf, X, Y):
    
    hit = 0
    miss = 0
    
    for x, y in zip(X, Y):
        if clf.predict([x])[0] == y:
            hit += 1
        else:
            miss += 1
    
    score = hit / len(X)*100
    
    print("Accuracy: %.1lf%% (%d hit / %d miss)" % (score, hit, miss))

def main():
    
    X_train, Y_train = read_data('data/train.txt')
    
    X_test, Y_test = read_data('data/test.txt')
    
    clf = train_MLP_classifier(X_train,Y_train)
    
    score = report_clf_stats(clf,X_test,Y_test)
    
    visualize(clf, X_test, Y_test)

if __name__ == "__main__":
    main()