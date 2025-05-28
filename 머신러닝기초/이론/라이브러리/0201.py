import numpy as np

x=[[1,2,3], [4,5,6], [7,8,9]]

def solution(data):

    array1 = np.array(x)

    array2 = np.zeros([3,3])

    array3 = np.ones([2,5])

    array4 = np.random.random([5,3])   

    array5 = np.arange(10)
    
    return array1, array2, array3, array4, array5

def print_answer(**kwargs):
    for key in kwargs.keys():
        print(key,"\n", kwargs[key], "\n")

array1, array2, array3, array4, array5 = solution(x)

print_answer(array1=array1, array2=array2, array3=array3, array4=array4, array5=array5)