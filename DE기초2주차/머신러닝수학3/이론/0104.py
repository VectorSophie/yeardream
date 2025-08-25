import numpy as np
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

A = np.array([[1,2],[2,0]])

u, s, vh = np.linalg.svd(A)

print('left-singular vectors: \n{}\n'.format(u))
print('Singular values: \n{}\n'.format(s))
print('right-singular vectors: \n{}\n'.format(vh))

u1 = u[:,0]
u2 = u[:,1]

vh1 = vh[0]
vh2 = vh[1]

Au1 = np.dot(A,u1)
Au2 = np.dot(A,u2)

origin = [0], [0]
plt.quiver(*origin, [u1[0],u2[0],Au1[0],Au2[0]], [u1[1],u2[1],Au1[1],Au2[1]], color=['r','b','g','c'], angles='xy', scale_units='xy',scale=1)
plt.axis([-5,5,-5,5])
plt.grid(True)
plt.savefig("image.png")
elice_utils.send_image("image.png")

vh1Au1 = np.dot(vh1,Au1)
vh2Au2 = np.dot(vh2,Au2)

print('vh1Au1: \n{}\n'.format(vh1Au1))
print('vh2Au2: \n{}\n'.format(vh2Au2))