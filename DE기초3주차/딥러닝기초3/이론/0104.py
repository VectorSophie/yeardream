import tensorflow as tf

import logging, os
logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

def make_model_relu():
    
    model_relu = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(64,activation='relu'),
        tf.keras.layers.Dense(32,activation='relu'),
        tf.keras.layers.Dense(32,activation='relu'),
        tf.keras.layers.Dense(32,activation='relu'),
        tf.keras.layers.Dense(32,activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    return model_relu

def make_model_sig():
    
    model_sig = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(64,activation='sigmoid'),
        tf.keras.layers.Dense(64,activation='sigmoid'),
        tf.keras.layers.Dense(64,activation='sigmoid'),
        tf.keras.layers.Dense(64,activation='sigmoid'),
        tf.keras.layers.Dense(64,activation='sigmoid'),
        tf.keras.layers.Dense(64,activation='sigmoid'),
        tf.keras.layers.Dense(32,activation='sigmoid'),
        tf.keras.layers.Dense(32,activation='sigmoid'),
        tf.keras.layers.Dense(32,activation='sigmoid'),
        tf.keras.layers.Dense(32,activation='sigmoid'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    return model_sig

def main():
    
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    
    model_relu = make_model_relu() 
    model_sig = make_model_sig()  
    
    model_relu.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    model_sig.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    
    model_relu.summary()
    model_sig.summary()
    
    model_relu_history = model_relu.fit(x_train,y_train,epochs=5,batch_size=500,verbose=0)
    print('\n')
    model_sig_history = model_sig.fit(x_train,y_train,epochs=5,batch_size=500,verbose=0)
    
    scores_relu = model_relu.evaluate(x_test,y_test,verbose=0)
    scores_sig = model_sig.evaluate(x_test,y_test,verbose=0)
    
    print('\naccuracy_relu: ', scores_relu[-1])
    print('accuracy_sig: ', scores_sig[-1])
    
    return model_relu_history, model_sig_history

if __name__ == "__main__":
    main()