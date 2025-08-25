import numpy as np
import tensorflow as tf
from visual import *

import logging, os
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

tf.random.set_seed(123)

def sequences_shaping(sequences, dimension):
    
    results = np.zeros((len(sequences), dimension))
    for i, word_indices in enumerate(sequences):
        results[i, word_indices] = 1.0 
        
    return results

def GD_model(word_num):
    
    model = tf.keras.Sequential([
    tf.keras.layers.Dense(32,input_shape=(word_num,),activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
    ])
    
    return model

def SGD_model(word_num):
    
    model = tf.keras.Sequential([
    tf.keras.layers.Dense(32,input_shape=(word_num,),activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
    ])
    
    return model

def main():
    
    word_num = 100
    data_num = 25000
    
    (train_data, train_labels), (test_data, test_labels) = tf.keras.datasets.imdb.load_data(num_words = word_num)
    
    train_data = sequences_shaping(train_data, dimension = word_num)
    test_data = sequences_shaping(test_data, dimension = word_num)
    
    gd_model = GD_model(word_num)  
    sgd_model = SGD_model(word_num) 
    
    gd_model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy','binary_crossentropy'])
    sgd_model.compile(loss='binary_crossentropy',optimizer='sgd',metrics=['accuracy','binary_crossentropy'])
    
    gd_model.summary()
    sgd_model.summary()
    
    gd_history = gd_model.fit(train_data, train_labels, epochs = 20, batch_size = data_num, validation_data = (test_data, test_labels), verbose = 0)
    print('\n')
    sgd_history = sgd_model.fit(train_data, train_labels, epochs = 20, batch_size = 500, validation_data = (test_data, test_labels), verbose = 0)
    
    scores_gd = gd_history.history['val_binary_crossentropy'][-1]
    scores_sgd = sgd_history.history['val_binary_crossentropy'][-1]
    
    print('\nscores_gd: ', scores_gd)
    print('scores_sgd: ', scores_sgd)
    
    Visulaize([('GD', gd_history),('SGD', sgd_history)])
    
    return gd_history, sgd_history

if __name__ == "__main__":
    main()