import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def constant_tensors():
    
    t1 = tf.constant(5,shape=(1,1),dtype=tf.int8)
    
    t2 = tf.zeros(shape=(3,5),dtype=tf.int16)
    
    t3 = tf.ones(shape=(4,3),dtype=tf.int8)
    
    return t1, t2, t3

def sequence_tensors():
    
    seq_t1 = tf.range(1.5,11,4.5)
    
    seq_t2 = tf.range(2.5,21,4.5)
    
    return seq_t1, seq_t2

def variable_tensor():
    
    var_tensor = tf.Variable(initial_value=100)
    
    W = tf.Variable(tf.ones(shape=(2,2)),name='W')
    
    b = tf.Variable(tf.zeros(shape=(2,)),name='b')
    
    return var_tensor, W, b

def main():
    
    t1, t2, t3 = constant_tensors()
    
    seq_t1,seq_t2 = sequence_tensors()
    
    var_tensor, W, b = variable_tensor()
    
    constant_dict = {'t1':t1, 't2':t2, 't3':t3}
    
    sequence_dict = {'seq_t1':seq_t1, 'seq_t2':seq_t2}
    
    variable_dict = {'var_tensor':var_tensor, 'W':W, 'b':b}
    
    for key, value in constant_dict.items():
        print(key, ' :', value.numpy())
    
    print()
    
    for key, value in sequence_dict.items():
        print(key, ' :', value.numpy())
        
    print()
    
    for key, value in variable_dict.items():
        print(key, ' :', value.numpy())

if __name__ == "__main__":
    main()