import numpy as np
from visual import *

np.random.seed(100)

def sigmoid(x):
    result = 1 / (1 + np.exp(-x))
    return result

def main():
    
    x_1 = np.random.randn(1000,100)
    x_2 = np.random.randn(1000,100)
    
    node_num = 100
    hidden_layer_size = 5
    
    activations_1 = {}
    activations_2 = {}
    
    for i in range(hidden_layer_size):
        if i != 0:
            x_1 = activations_1[i-1]
            x_2 = activations_2[i-1]
        
        w_1 = np.random.randn(100,100)
        w_2 = np.random.randn(100,100) *0.01
        
        a_1 = np.dot(x_1,w_1)
        a_2 = np.dot(x_2,w_2)
        
        z_1 = sigmoid(a_1)
        z_2 = sigmoid(a_2)
        
        activations_1[i] = z_1
        activations_2[i] = z_2
        
    Visual(activations_1,activations_2)
    
    return activations_1, activations_2

if __name__ == "__main__":
    main()