import numpy as np
import logging, os

logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

def tf1():
    
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()
    
    a = tf.constant(5)
    b = tf.constant(3)
    
    add_op = a+b
    
    sess = tf.Session()
    result_tf1 = sess.run(add_op)
    
    return a, b, result_tf1

def tf2():
    
    import tensorflow as tf
    tf.compat.v1.enable_v2_behavior()
    
    a = tf.constant(5)
    b = tf.constant(3)
    
    result_tf2 = tf.add(a,b)
    
    return a, b, result_tf2.numpy()

def main():
    
    tf_2, tf_1 = tf2()[2], tf1()[2]
    
    print('result_tf1:', tf_1)
    print('result_tf2:', tf_2)
    
if __name__ == "__main__":
    main()