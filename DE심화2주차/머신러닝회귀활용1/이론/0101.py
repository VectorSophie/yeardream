import numpy as np
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def load_data():
    
    X = np.array([[8.70153760], [3.90825773], [1.89362433], [3.28730045], [7.39333004], [2.98984649], [2.25757240], [9.84450732], [9.94589513], [5.48321616]])
    y = np.array([[5.64413093], [3.75876583], [3.87233310], [4.40990425], [6.43845020], [4.02827829], [2.26105955], [7.15768995], [6.29097441], [5.19692852]])
    
    return X, y

def prediction(beta_0, beta_1, X):
    
    y_pred = beta_0 + beta_1 * X
    
    return y_pred

def update_beta(X, y, y_pred, lr):
    
    delta_0 = -(lr * (2 / len(X)) * np.sum(y - y_pred))
    
    delta_1 = -(lr * (2 / len(X)) * (np.dot(X.T, (y - y_pred))))
    
    return delta_0, delta_1

def gradient_descent(X, y, iters, lr):
    
    beta_0 = np.zeros((1,1))
    beta_1 = np.zeros((1,1))
    
    for i in range(iters):
        
        y_pred = prediction(beta_0, beta_1, X)
        loss = np.mean(np.square(y - y_pred))
        
        beta0_delta, beta1_delta = update_beta(X, y, y_pred, lr)
        
        beta_0 -= beta0_delta
        beta_1 -= beta1_delta
        
        if i%100==0:
            print("학습 횟수 :",i)
            plotting_graph(X,y,beta_0,beta_1)
        
    return beta_0, beta_1

def plotting_graph(X,y,beta_0,beta_1):
    
    y_pred = beta_0 + beta_1[0,0] * X
    
    fig = plt.figure()
    
    plt.scatter(X, y)
    plt.plot(X, y_pred,c='r')
    
    plt.savefig("test.png")
    elice_utils.send_image("test.png")

def main():
    
    lr = 1e-4
    iteration = 1000
    
    X, y = load_data()
    
    beta_0, beta_1 = gradient_descent(X, y, iteration, lr)
    
    print("{}번의 학습 이후의 회귀 알고리즘 결과".format(iteration))
    print("beta_0:",beta_0[0], "beta_1:",beta_1[0])
    
    plotting_graph(X,y,beta_0,beta_1)
    
    return beta_0, beta_1

if __name__=="__main__":
    main()