import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def insert():
    
    x = float(input('정수 또는 실수를 입력하세요. x : '))
    y = float(input('정수 또는 실수를 입력하세요. y : '))
    cal = input('어떤 연산을 할것인지 입력하세요. (+, -, *, /)')
    
    return x, y, cal

def calcul(x,y,cal):

    result = 0
    
    if cal == '+':
        result = tf.add(x, y)
    elif cal == '-':
        result = tf.subtract(x, y)
    elif cal == '*':
        result = tf.multiply(x, y)
    elif cal == '/':
        result = tf.truediv(x, y)
    
    return result.numpy()

def main():
    
    x, y, cal = insert()
    
    print(calcul(x,y,cal))

if __name__ == "__main__":
    main()