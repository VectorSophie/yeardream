from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

def load_data():
    
    X, y = load_wine(return_X_y = True)
    
    print("데이터 확인해보기 :\n", X[:1])
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)
    
    return train_X, test_X, train_y, test_y

def Gaussian_NB(train_X, test_X, train_y, test_y):
    
    model = GaussianNB()
    
    model.fit(train_X, train_y)

    predicted = model.predict(test_X)
    
    return predicted

def main():
    
    train_X, test_X, train_y, test_y = load_data()
    
    predicted = Gaussian_NB(train_X, test_X, train_y, test_y)

    print("\nModel Accuracy : ")
    print(accuracy_score(test_y, predicted))

if __name__ == "__main__":
    main()
