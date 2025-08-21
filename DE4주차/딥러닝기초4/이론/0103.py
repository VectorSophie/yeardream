import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from visual import *
from plotter import *

import logging, os
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

np.random.seed(123)
tf.random.set_seed(123)


def preprocess():
    
    mnist = tf.keras.datasets.mnist
    
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()    
    
    train_images, train_labels = train_images[:5000], train_labels[:5000]
    test_images, test_labels = test_images[:1000], test_labels[:1000]
    
    train_images = train_images/255
    test_images = test_images/255
    
    train_images = np.expand_dims(train_images,-1)
    test_images = np.expand_dims(test_images,-1)
    
    train_labels = to_categorical(train_labels)
    test_labels = to_categorical(test_labels)
    
    return train_images, test_images, train_labels, test_labels

def CNN():
    
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3), activation='relu',padding='SAME',input_shape=(28,28,1)))
    model.add(tf.keras.layers.MaxPool2D(padding='SAME'))
    model.add(tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3), activation='relu',padding='SAME'))
    model.add(tf.keras.layers.MaxPool2D(padding='SAME'))
    model.add(tf.keras.layers.Conv2D(filters=32,kernel_size=(3,3), activation='relu',padding='SAME'))
    model.add(tf.keras.layers.MaxPool2D(padding='SAME'))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(64,activation='relu'))
    model.add(tf.keras.layers.Dense(32,activation='relu'))
    model.add(tf.keras.layers.Dense(10,activation='softmax'))
    
    return model

def main():
    
    train_images, test_images, train_labels, test_labels = preprocess()
    
    model = CNN()
    
    model.summary()
    
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    
    history = model.fit(train_images,train_labels,epochs=15,batch_size=128,validation_data=(test_images,test_labels),verbose=2)
    
    loss, test_acc = model.evaluate(test_images,test_labels,verbose=0)
    
    print('\nTest Loss : {:.4f} | Test Accuracy : {}'.format(loss, test_acc))
    print('예측한 Test Data 클래스 : ',model.predict_classes(test_images)[:10])
    
    Visulaize([('CNN', history)], 'loss')
    
    Plotter(test_images, model)
    
    return history
    
if __name__ == "__main__":
    main()