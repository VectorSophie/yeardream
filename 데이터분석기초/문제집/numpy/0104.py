import numpy as np

print("array")
array = np.arange(8)
print(array)
print("shape : ", array.shape, "\n")

print("# reshape (2, 4)")
matrix = array.reshape(2,4)

print(matrix)
print("shape : ", matrix.shape)