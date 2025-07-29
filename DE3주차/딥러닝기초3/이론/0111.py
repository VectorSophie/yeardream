import numpy as np
import tensorflow as tf
from visual import *

import logging, os
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def sequences_shaping(sequences, dimension):
    
    results = np.zeros((len(sequences), dimension))
    for i, word_indices in enumerate(sequences):
        results[i, word_indices] = 1.0 
        
    return results

def Basic(word_num):
    
    basic_model = tf.keras.Sequential([tf.keras.layers.Dense(128,input_shape=(word_num,),activation='relu'),tf.keras.layers.Dense(128, activation='relu'),tf.keras.layers.Dense(1, activation='sigmoid')])
    
    return basic_model

def Dropout(word_num):
    
    dropout_model = tf.keras.Sequential([tf.keras.layers.Dense(128,input_shape=(word_num,),activation='relu'),tf.keras.layers.Dropout(0.3),tf.keras.layers.Dense(128, activation='relu'),tf.keras.layers.Dropout(0.3),tf.keras.layers.Dense(1, activation='sigmoid')])
    
    return dropout_model

def main():
    
    word_num = 100
    data_num = 25000
    
    (train_data, train_labels), (test_data, test_labels) = tf.keras.datasets.imdb.load_data(num_words = word_num)
    
    train_data = sequences_shaping(train_data, dimension = word_num)
    test_data = sequences_shaping(test_data, dimension = word_num)
    
    basic_model = Basic(word_num)    
    dropout_model = Dropout(word_num)  
    
    basic_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_crossentropy'])
    dropout_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_crossentropy'])

    basic_model.summary()
    dropout_model.summary()
    
    basic_history = basic_model.fit(train_data, train_labels, epochs=20, batch_size=500, validation_data=(test_data, test_labels), verbose=0)
    print('\n')
    dropout_history = dropout_model.fit(train_data, train_labels, epochs=20, batch_size=500, validation_data=(test_data, test_labels), verbose=0)
    
    scores_basic = basic_model.evaluate(test_data,test_labels,verbose=0)
    scores_dropout = dropout_model.evaluate(test_data,test_labels,verbose=0)
    
    print('\nscores_basic: ', scores_basic[-1])
    print('scores_dropout: ', scores_dropout[-1])
    
    Visulaize([('Basic', basic_history),('Dropout', dropout_history)])
    
    return basic_history, dropout_history

if __name__ == "__main__":
    main()