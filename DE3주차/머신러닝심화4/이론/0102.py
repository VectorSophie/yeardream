from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def load_data():
    
    X, y = load_iris(return_X_y=True)
    
    train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.2,random_state=100)
    
    return train_X, test_X, train_y, test_y

def DT_Clf(train_X, train_y, test_X):
    
    clf = DecisionTreeClassifier()
    
    clf.fit(train_X,train_y)
    
    pred = clf.predict(test_X)
    
    return pred

def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    pred = DT_Clf(train_X, train_y, test_X)
    print('테스트 데이터에 대한 예측 정확도 : {0:.4f}'.format(accuracy_score(test_y, pred)))
    
    return pred
    
if __name__ == "__main__":
    main()
