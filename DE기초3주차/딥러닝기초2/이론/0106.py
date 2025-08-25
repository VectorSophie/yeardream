import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from elice_utils import EliceUtils
elice_utils = EliceUtils()

np.random.seed(100)

class LinearModel:
    
    def __init__(self):
        
        self.W = tf.Variable(1.5)
        
        self.b = tf.Variable(1.5)
        
    def __call__(self, X, Y):
        
        return tf.add(tf.multiply(X,self.W),self.b)

def loss(y, pred):
    
    return tf.reduce_mean(tf.square(y-pred))

def train(linear_model, x, y):
    
    with tf.GradientTape() as t:
        current_loss = loss(y, linear_model(x, y))
    
    learning_rate = 0.001
    
    delta_W, delta_b = t.gradient(current_loss, [linear_model.W, linear_model.b])
    
    W_update = (learning_rate * delta_W)
    b_update = (learning_rate * delta_b)
    
    return W_update,b_update
 
def main():
    
    x_data = np.linspace(0, 10, 50)
    y_data = 4 * x_data + np.random.randn(*x_data.shape)*4 + 3
    
    # 데이터 출력
    plt.scatter(x_data,y_data)
    plt.savefig('data.png')
    elice_utils.send_image('data.png')
    
    linear_model = LinearModel()
    
    epochs = 100
    
    for epoch_count in range(epochs):
        
        y_pred_data=linear_model(x_data, y_data)
        
        real_loss = loss(y_data, linear_model(x_data, y_data))
        
        update_W, update_b = train(linear_model, x_data, y_data)
        
        linear_model.W.assign_sub(update_W)
        linear_model.b.assign_sub(update_b)
        
        if (epoch_count%20==0):
            print(f"Epoch count {epoch_count}: Loss value: {real_loss.numpy()}")
            print('W: {}, b: {}'.format(linear_model.W.numpy(), linear_model.b.numpy()))
            
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax1.scatter(x_data,y_data)
            ax1.plot(x_data,y_pred_data, color='red')
            plt.savefig('prediction.png')
            elice_utils.send_image('prediction.png')

if __name__ == "__main__":
    main()