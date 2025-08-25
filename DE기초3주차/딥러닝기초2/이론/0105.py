import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def main():
    
    a = tf.constant(10, dtype = tf.int32)
    b = tf.constant(3, dtype = tf.int32)
    
    add = tf.add(a,b)
    sub = tf.subtract(a,b)
    mul = tf.multiply(a,b)
    div = tf.truediv(a,b)
    
    tensor_dict = {'add':add, 'sub':sub, 'mul':mul, 'div':div}
    
    for key, value in tensor_dict.items():
        print(key, ' :', value.numpy(), '\n')
    
    return add, sub, mul, div

if __name__ == "__main__":
    main()