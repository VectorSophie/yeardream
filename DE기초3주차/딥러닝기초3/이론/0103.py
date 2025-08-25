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

def OPT_model(word_num):
    
    model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, input_shape=(word_num,), activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')])
    
    return model

def main():
    
    word_num = 100
    data_num = 25000
    
    (train_data, train_labels), (test_data, test_labels) = tf.keras.datasets.imdb.load_data(num_words = word_num)
    
    train_data = sequences_shaping(train_data, dimension = word_num)
    test_data = sequences_shaping(test_data, dimension = word_num)
    
    adagrad_model = OPT_model(word_num)  
    rmsprop_model = OPT_model(word_num)  
    adam_model = OPT_model(word_num) 
    
    adagrad_opt = tf.keras.optimizers.Adagrad(learning_rate=0.01, epsilon=1e-5, decay=0.4)
    adagrad_model.compile(loss='binary_crossentropy', optimizer=adagrad_opt, metrics=['accuracy', 'binary_crossentropy'])
    
    rmsprop_opt = tf.keras.optimizers.RMSprop(learning_rate=0.001)
    rmsprop_model.compile(loss='binary_crossentropy', optimizer=rmsprop_opt, metrics=['accuracy', 'binary_crossentropy'])
    
    adam_opt = tf.keras.optimizers.Adam(learning_rate=0.01, beta_1=0.9, beta_2=0.999)
    adam_model.compile(loss='binary_crossentropy', optimizer=adam_opt, metrics=['accuracy', 'binary_crossentropy'])
    
    adagrad_model.summary()
    rmsprop_model.summary()
    adam_model.summary()

    adagrad_history = adagrad_model.fit(train_data, train_labels, epochs=20, batch_size=500, validation_data=(test_data,test_labels), verbose=0)
    print('\n')
    rmsprop_history = rmsprop_model.fit(train_data, train_labels, epochs=20, batch_size=500, validation_data=(test_data,test_labels), verbose=0)
    print('\n')
    adam_history = adam_model.fit(train_data, train_labels, epochs=20, batch_size=500, validation_data=(test_data,test_labels), verbose=0)
    
    scores_adagrad = adagrad_model.evaluate(test_data, test_labels)
    scores_rmsprop = rmsprop_model.evaluate(test_data, test_labels)
    scores_adam = adam_model.evaluate(test_data, test_labels)
    
    print('\nscores_adagrad: ', scores_adagrad[-1])
    print('scores_rmsprop: ', scores_rmsprop[-1])
    print('scores_adam: ', scores_adam[-1])
    
    Visulaize([('Adagrad', adagrad_history),('RMSprop', rmsprop_history),('Adam', adam_history)])
    
    return adagrad_history, rmsprop_history, adam_history
    
if __name__ == "__main__":
    main()