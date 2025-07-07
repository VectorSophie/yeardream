import tensorflow as tf
import numpy as np
from visual import *

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

np.random.seed(100)
tf.random.set_seed(100)

def main():
    
    x_data = np.linspace(0, 10, 100)
    y_data = 1.5 * x_data**2 -12 * x_data + np.random.randn(*x_data.shape)*2 + 0.5
    
    model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(20, input_dim = 1 ,activation='relu'),
    tf.keras.layers.Dense(20, activation='relu'),
    tf.keras.layers.Dense(1)
    ])

    model.compile(loss ='mean_squared_error', optimizer = 'adam') 
    
    history = model.fit(x_data,y_data,epochs=500,verbose=2)

    predictions = model.predict(x_data)
    
    Visualize(x_data, y_data, predictions)
    
    return history, model

if __name__ == '__main__':
    main()