import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

A = np.array([[1,2],[2,0]])

w,v = np.linalg.eig(A)

print('eigen value: {}\n'.format(w))
print('eigen vector: \n{}\n'.format(v))

v1 = v[:,0]
v2 = v[:,1]

Av1 = np.dot(A,v1)
Av2 = np.dot(A,v2)

origin = [0], [0]
plt.quiver(*origin, [v1[0],v2[0],Av1[0],Av2[0]], [v1[1],v2[1],Av1[1],Av2[1]], color=['r','b','g','c'], angles='xy', scale_units='xy',scale=1)
plt.axis([-5,5,-5,5])
plt.grid(True)
plt.savefig("image.png")
elice_utils.send_image("image.png")