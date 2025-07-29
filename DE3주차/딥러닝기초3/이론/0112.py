import numpy as np
import tensorflow as tf

import matplotlib.pyplot as plt

import logging
import os

from elice_utils import EliceUtils
elice_utils = EliceUtils()

logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

np.random.seed(42)
tf.random.set_seed(42)

def generate_basic_model():
    basic_model = tf.keras.Sequential([
                  tf.keras.layers.Flatten(input_shape=(28, 28)),
                  tf.keras.layers.Dense(128),
                  tf.keras.layers.Activation('relu'),
                  tf.keras.layers.Dense(128),
                  tf.keras.layers.Dense(10, activation='softmax')])
    return basic_model


def generate_batch_norm_model():

    bn_model = tf.keras.Sequential([
                tf.keras.layers.Flatten(input_shape=(28, 28)),
                tf.keras.layers.Dense(128),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.Activation('relu'),
                tf.keras.layers.Dense(128),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.Dense(10, activation='softmax')])
    return bn_model


def main():
 
    mnist = tf.keras.datasets.mnist
    (train_data, train_labels), (test_data, test_labels) = mnist.load_data()
    train_data, test_data = train_data / 255.0, test_data / 255.0

    base_model = generate_basic_model()
    bn_model = generate_batch_norm_model()

    base_model.summary()
    bn_model.summary()

    base_model.compile(optimizer='adam',
                       loss='sparse_categorical_crossentropy',
                       metrics=['accuracy'])
    bn_model.compile(optimizer='adam',
                     loss='sparse_categorical_crossentropy',

                     metrics=['accuracy'])
    
    base_history = base_model.fit(train_data, train_labels, epochs=10,
                                  validation_data=(test_data, test_labels))
    bn_history = bn_model.fit(train_data, train_labels, epochs=10, 
                              validation_data=(test_data, test_labels))
    
    plt.plot(base_history.history['val_loss'], label='base model')
    plt.plot(bn_history.history['val_loss'], label='batch norm model')
    plt.xlabel('Epoch')
    plt.ylabel('Validation Loss')
    plt.ylim([0.05, 0.15])
    plt.legend(loc='lower right')

    plt.savefig("plot.png")
    elice_utils.send_image("plot.png")


    return base_model, bn_model

if __name__ == "__main__":
    main()