import numpy as np
from numpy.linalg import solve
import math

A = np.array([
    [8.0,-4.0,-2.0],
    [-4.0,10.0,-2.0],
    [-2.0,-2.0,10.0]
])
B = np.array(
    [[10.0],
     [0.0],
     [40],
     ]
)
Ac=A
A = np.concatenate((A, B), axis=1)


def triangular_superior(A,B):

    n=np.size(B)
    for k in range(0,n-1):
         for i in range(k+1,n):

                m = A[i,k]/A[k,k]

                A[i,:]=A[i,:] - m*A[k,:]
    print(A.round())
    return(A)
size=np.size(A,axis=1)
print(size)
resultado=triangular_superior(A,B)
B= A[:,size-1]
x=solve(Ac,B).round()

print("O resultado é: {}".format(x))