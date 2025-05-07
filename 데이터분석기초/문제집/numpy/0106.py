import numpy as np

print("matrix")
matrix = np.array([[ 0, 1, 2, 3],
                   [ 4, 5, 6, 7],
                   [ 8, 9,10,11], 
                   [12,13,14,15]])
print(matrix, "\n")

a, b = np.split(matrix,[3],axis=0)

print(a, "\n")
print(b, "\n")

c, d = np.split(matrix,[1],axis=1)

print(c, "\n")
print(d)