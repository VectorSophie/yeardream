import numpy as np
from visual import *

np.random.seed(100)
    
def relu(x):
    result = np.maximum(0,x)
    return result

def main():
    
    x_relu = np.random.randn(1000,100)
    
    node_num = 100
    hidden_layer_size = 5
    
    activations_relu = {}
    
    for i in range(hidden_layer_size):
        if i != 0:
            x_relu = activations_relu[i-1]
            
        w_relu = np.random.randn(100,100)*np.sqrt(2/node_num)
        
        a_relu = np.dot(x_relu,w_relu)
        
        z_relu = relu(a_relu)
        
        activations_relu[i] = z_relu
        
    Visual(activations_relu)
    
    return activations_relu    

if __name__ == "__main__":
    main()