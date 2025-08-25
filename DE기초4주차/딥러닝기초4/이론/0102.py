import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from visual import *

import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

np.random.seed(123)
tf.random.set_seed(123)

def preprocess():
    
    mnist = tf.keras.datasets.mnist
    
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()    
    
    train_images = train_images / 255
    test_images  = test_images / 255
    
    train_labels = to_categorical(train_labels, 10)
    test_labels  = to_categorical(test_labels, 10)
    
    return train_images, test_images, train_labels, test_labels

def MLP():
    
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
    model.add(tf.keras.layers.Dense(128, activation='relu'))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))
    
    return model

def main():
    
    train_images, test_images, train_labels, test_labels = preprocess()
    
    model = MLP()
    
    model.compile(
        loss="categorical_crossentropy",
        optimizer="adam",
        metrics=["accuracy"]
    )
    
    model.summary()
    
    history = model.fit(
        train_images, train_labels,
        epochs=20,            
        batch_size=128,
        validation_data=(test_images, test_labels), verbose=2
    )
    
    loss, test_acc = model.evaluate(test_images, test_labels, verbose=0)
    print('\nTest Loss : {:.4f} | Test Accuracy : {:.4f}'.format(loss, test_acc))
    
    print('예측한 Test Data 클래스 : ',model.predict_classes(test_images))
    
    Visulaize([('MLP', history)], 'loss')
    
    return history
    
if __name__ == "__main__":
    main()