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
    
    basic_model = tf.keras.Sequential([tf.keras.layers.Dense(128,input_shape=(word_num,),activation='relu'),tf.keras.layers.Dense(128,activation='relu'),tf.keras.layers.Dense(1,activation='sigmoid')])
    
    return basic_model


def L1(word_num):
    
    l1_model = tf.keras.Sequential([tf.keras.layers.Dense(128,input_shape=(word_num,),activation='relu',kernel_regularizer=tf.keras.regularizers.l1(0.001)),tf.keras.layers.Dense(128,activation='relu',kernel_regularizer=tf.keras.regularizers.l1(0.001)),tf.keras.layers.Dense(1,activation='sigmoid')])
    
    return l1_model


def L2(word_num):
    
    l2_model = tf.keras.Sequential([tf.keras.layers.Dense(128,input_shape=(word_num,),activation='relu',kernel_regularizer=tf.keras.regularizers.l2(0.001)),tf.keras.layers.Dense(128,activation='relu',kernel_regularizer=tf.keras.regularizers.l2(0.001)),tf.keras.layers.Dense(1,activation='sigmoid')])
    
    return l2_model


def main():
    
    word_num = 100
    data_num = 25000
    
    (train_data, train_labels), (test_data, test_labels) = tf.keras.datasets.imdb.load_data(num_words = word_num)
    
    train_data = sequences_shaping(train_data, dimension = word_num)
    test_data = sequences_shaping(test_data, dimension = word_num)
    
    basic_model = Basic(word_num)  
    l1_model = L1(word_num)   
    l2_model = L2(word_num)    
    
    basic_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_crossentropy'])
    l1_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_crossentropy'])
    l2_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy','binary_crossentropy'])
    
    basic_model.summary()
    l1_model.summary()
    l2_model.summary()
    
    basic_history = basic_model.fit(train_data,train_labels,epochs=20,batch_size=500,validation_data=(test_data,test_labels),verbose=0)
    print('\n')
    l1_history = l1_model.fit(train_data,train_labels,epochs=20,batch_size=500,validation_data=(test_data,test_labels),verbose=0)
    print('\n')
    l2_history = l2_model.fit(train_data,train_labels,epochs=20,batch_size=500,validation_data=(test_data,test_labels),verbose=0)
    
    scores_basic = basic_model.evaluate(test_data,test_labels,verbose=0)
    scores_l1 = l1_model.evaluate(test_data,test_labels,verbose=0)
    scores_l2 = l2_model.evaluate(test_data,test_labels,verbose=0)
    
    print('\nscores_basic: ', scores_basic[-1])
    print('scores_l1: ', scores_l1[-1])
    print('scores_l2: ', scores_l2[-1])
    
    Visulaize([('Basic', basic_history),('L1 Regularization', l1_history), ('L2 Regularization', l2_history)])
    
    return basic_history, l1_history, l2_history

if __name__ == "__main__":
    main()              