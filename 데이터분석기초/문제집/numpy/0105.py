import numpy as np

print("matrix")
matrix = np.array([[0,1,2,3],
                   [4,5,6,7]])
print(matrix)
print("shape : ", matrix.shape, "\n")

m = np.concatenate([matrix,matrix],axis=0)
n = np.concatenate([matrix,matrix],axis=1)