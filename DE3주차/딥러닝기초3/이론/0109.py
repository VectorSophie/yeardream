import numpy as np
import tensorflow as tf
from visual import *

import logging, os
logging.disable(logging.WARNING) 

def sequences_shaping(sequences, dimension):
    
    results = np.zeros((len(sequences), dimension))
    for i, word_indices in enumerate(sequences):
        results[i, word_indices] = 1.0 
        
    return results

def Basic(word_num):
    
    basic_model = tf.keras.Sequential([tf.keras.layers.Dense(256, activation = 'relu', input_shape=(word_num,)), tf.keras.layers.Dense(128, activation = 'relu'), tf.keras.layers.Dense(1, activation= 'sigmoid')])
    
    return basic_model

def Overfitting(word_num):
    
    overfit_model = tf.keras.Sequential([ tf.keras.layers.Dense(1024, activation = 'relu', input_shape=(word_num,)), tf.keras.layers.Dense(512, activation = 'relu'),tf.keras.layers.Dense(512, activation = 'relu'),tf.keras.layers.Dense(512, activation = 'relu'),
tf.keras.layers.Dense(1, activation= 'sigmoid')])
    
    return overfit_model


def main():
    
    word_num = 100
    data_num = 25000
    
    (train_data, train_labels), (test_data, test_labels) = tf.keras.datasets.imdb.load_data(num_words = word_num)
    
    train_data = sequences_shaping(train_data, dimension = word_num)
    test_data = sequences_shaping(test_data, dimension = word_num)
    
    basic_model = Basic(word_num)   
    overfit_model = Overfitting(word_num)  

    basic_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_crossentropy'])
    overfit_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_crossentropy'])
    
    basic_model.summary()
    overfit_model.summary()
    
    basic_history = basic_model.fit(train_data,train_labels,epochs=20,batch_size=500,validation_data=(test_data,test_labels),verbose=0)
    print('\n')
    overfit_history = overfit_model.fit(train_data,train_labels,epochs=20,batch_size=500,validation_data=(test_data,test_labels),verbose=0)
    
    scores_basic = basic_model.evaluate(test_data,test_labels,verbose=0)
    scores_overfit = overfit_model.evaluate(test_data,test_labels,verbose=0)
    
    print('\nscores_basic: ', scores_basic[-1])
    print('scores_overfit: ', scores_overfit[-1])
    
    Visualize([('Basic', basic_history),('Overfitting', overfit_history)])
    
    return basic_history, overfit_history

if __name__ == "__main__":
    main()