import numpy as np

def linear_model(w0, w1, X):
    
    f_x = w0 + w1 * X
    
    return f_x

def Loss(f_x, y):
    
    ls = np.mean(np.square(y-f_x))
    
    return ls

def gradient_descent(w0, w1, X, y):
    
    gradient0 = 2*np.mean((y-(w0+w1*X))*(-1))
    gradient1 = 2*np.mean((y-(w0+w1*X))*(-1*X))
    
    return np.array([gradient0, gradient1])

def main():
    
    X = np.array([1,2,3,4]).reshape((-1,1))
    y = np.array([3.1, 4.9, 7.2, 8.9]).reshape((-1,1))
    
    w0 = 0
    w1 = 0
    
    lr = 0.001
    
    for i in range(1000):
    
        gd = gradient_descent(w0,w1,X,y)
        
        w0 = w0-lr*gd[0]
        w1 = w1-lr*gd[1]
        
        if (i % 100 == 0):
        
            loss = Loss(linear_model(w0,w1,X),y)
        
            print("{}번째 loss : {}".format(i, loss))
            print("{}번째 w0, w1 : {}, {}".format(i, w0, w1),'\n')

    return w0, w1

if __name__ == '__main__':
    main()