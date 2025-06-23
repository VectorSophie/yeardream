import sys
import warnings

import numpy as np
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings(action="ignore")
np.random.seed(100)

def load_data(X, y):

    X_train = X[:1600]
    Y_train = y[:1600]

    X_test = X[1600:]
    Y_test = y[1600:]

    return X_train, Y_train, X_test, Y_test


def train_MLP_classifier(X, y):

    clf = MLPClassifier(hidden_layer_sizes=(128,128), solver='adam', beta_1=0.999999)
    clf.fit(X, y)

    return clf


def report_clf_stats(clf, X, y):

    hit = 0
    miss = 0

    for x, y_ in zip(X, y):
        if clf.predict([x])[0] == y_:
            hit += 1
        else:
            miss += 1

    score = hit / len(X)*100

    print(f"Accuracy: {score:.1f} ({hit} hit / {miss} miss)")

    return score

def main():

    digits = load_digits()

    X = digits.data
    y = digits.target

    X_train, Y_train, X_test, Y_test = load_data(X,y)

    clf = train_MLP_classifier(X_train,Y_train)

    score = report_clf_stats(clf,X_test,Y_test)

    return score

if __name__ == "__main__":
    sys.exit(main())
