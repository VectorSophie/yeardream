import numpy as np
import tensorflow as tf
from keras.datasets import imdb
from keras.preprocessing import sequence

import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

np.random.seed(0)
tf.random.set_seed(0)

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

def load_data(n_of_training_ex, n_of_testing_ex, max_review_length):
    
    PATH = "./data/"
    
    X_train = np.load(PATH + "X_train.npy")[:n_of_training_ex]
    y_train = np.load(PATH + "y_train.npy")[:n_of_training_ex]
    X_test = np.load(PATH + "X_test.npy")[:n_of_testing_ex]
    y_test = np.load(PATH + "y_test.npy")[:n_of_testing_ex]
    
    X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
    X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
    
    return X_train, y_train, X_test, y_test
    
def SimpleRNN(embedding_vector_length, max_review_length):
    
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Embedding(input_dim=1000,output_dim=embedding_vector_length, input_length=max_review_length))
    model.add(tf.keras.layers.SimpleRNN(5))
    model.add(tf.keras.layers.Dense(1,activation='sigmoid'))
    
    return model

def LSTM(embedding_vector_length, max_review_length):
    
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Embedding(input_dim=1000,output_dim=embedding_vector_length, input_length=max_review_length))
    model.add(tf.keras.layers.LSTM(5))
    model.add(tf.keras.layers.Dense(1,activation='sigmoid'))
    
    return model

def GRU(embedding_vector_length, max_review_length):
    
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Embedding(input_dim=1000,output_dim=embedding_vector_length, input_length=max_review_length))
    model.add(tf.keras.layers.GRU(5))
    model.add(tf.keras.layers.Dense(1,activation='sigmoid'))
    
    return model

def main():
    
    max_review_length = 300
    embedding_vector_length = 32
    
    n_of_training_ex = 25000
    n_of_testing_ex = 3000
    
    X_train, y_train, X_test, y_test = load_data(n_of_training_ex, n_of_testing_ex, max_review_length)
    
    model_simple_rnn = SimpleRNN(embedding_vector_length, max_review_length)
    model_lstm = LSTM(embedding_vector_length, max_review_length)
    model_gru = GRU(embedding_vector_length, max_review_length)
    
    model_simple_rnn.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    model_lstm.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    model_gru.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    
    model_simple_rnn.summary()
    model_lstm.summary()
    model_gru.summary()
    
    model_simple_rnn_history = model_simple_rnn.fit(X_train,y_train,epochs=3,batch_size=256,verbose=0)
    print('\n')
    model_lstm_history = model_lstm.fit(X_train,y_train,epochs=3,batch_size=256,verbose=0)
    print('\n')
    model_gru_history = model_gru.fit(X_train,y_train,epochs=3,batch_size=256,verbose=0)
    
    scores_simple_rnn = model_simple_rnn.evaluate(X_test,y_test, verbose=0)
    scores_lstm = model_lstm.evaluate(X_test,y_test, verbose=0)
    scores_gru = model_gru.evaluate(X_test,y_test, verbose=0)
    
    print('\nTest Accuracy_simple rnn: ', scores_simple_rnn[-1])
    print('Test Accuracy_lstm: ', scores_lstm[-1])
    print('Test Accuracy_gru: ', scores_gru[-1])
    
    return model_simple_rnn_history, model_lstm_history, model_gru_history

if __name__ == '__main__':
    main()