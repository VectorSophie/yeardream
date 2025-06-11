import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def load_data():
    
    rng = np.random.RandomState(1)
    X = np.sort(5 * rng.rand(80, 1), axis=0)
    y = np.sin(X).ravel()
    y[::5] += 3 * (0.5 - rng.rand(16))
    
    return X, y

def DT_Reg(X, y, X_test, m_depth):
    
    reg = DecisionTreeRegressor(max_depth=m_depth)
    
    reg.fit(X,y)
    
    pred = reg.predict(X_test)
    
    return pred

def Visualize(X, y, X_test, y_1, y_5, y_20):
    
    plt.figure()
    plt.scatter(X, y, s=20, edgecolor="black",
                c="darkorange", label="data")
    plt.plot(X_test, y_1, color="cornflowerblue",
             label="max_depth=1", linewidth=2)
    plt.plot(X_test, y_5, color="yellowgreen", label="max_depth=5", linewidth=2)
    plt.plot(X_test, y_20, color="red", label="max_depth=20", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    
    plt.savefig('decision_regressor.png')
    elice_utils.send_image('decision_regressor.png')
    
def main():
    
    X, y = load_data()
    
    X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]

    y_1 = DT_Reg(X,y,X_test,m_depth=1)
    
    y_5 = DT_Reg(X,y,X_test,m_depth=5)

    y_20 = DT_Reg(X,y,X_test,m_depth=20)
    
    Visualize(X, y, X_test, y_1, y_5, y_20)
    
    return y_1, y_5, y_20
    
if __name__ == "__main__":
    main()
