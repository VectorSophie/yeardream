import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import KFold

def load_data():
    
    X, y = load_boston(return_X_y=True)
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=100)
    
    return train_X, test_X, train_y, test_y

def kfold_regression(train_X, train_y):
    
    n_iter = 0
    
    model_scores = []
    
    kfold = KFold(n_splits=5)
    
    for train_idx, val_idx in kfold.split(train_X):
        
        X_train, X_val = train_X[train_idx], train_X[val_idx]
        y_train, y_val = train_y[train_idx], train_y[val_idx]
        
        model = LinearRegression()
        
        model.fit(X_train, y_train)
        
        score = model.score(X_val, y_val)
        
        train_size = X_train.shape[0]
        val_size = X_val.shape[0]
    
        print("Iter : {0} Cross-Validation Accuracy : {1}, Train Data 크기 : {2}, Validation Data 크기 : {3}"
              .format(n_iter, score, train_size, val_size))
    
        n_iter += 1
        
        model_scores.append(score)
        
    return kfold, model, model_scores
        
        
def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    kfold, model, model_scores = kfold_regression(train_X, train_y)
    
    print("\n> 평균 검증 모델 점수 : ", np.mean(model_scores))
    
if __name__ == "__main__":
    main()
