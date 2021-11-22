import numpy as np
from numpy.linalg import solve

A=np.array([
[-4,-4,-7,-3],
[0,-1,5,2],
[0,0,-7,1],
[0,0,0,-1]
])
B=np.array(
    [[-47],[29],[-23],[-5]]
)
c=np.concatenate((A,B),axis=1)
x=solve(A,B)

print("A Matrix extendida é:")
print(c)
print ("-----------------------------------")
print("A primeira tupla corresponde a x1, a ultima tupla corresponde a xn")
print(x)

