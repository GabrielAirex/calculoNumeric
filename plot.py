import matplotlib.pyplot as plt

import numpy as np



def f(x):
    return ((15.26*x**2)/2)-0.5

def ft1(x):
    return 1.526*x-0.5763

def ft2(x):
    return 1.526*x-0.5763 + 7.63*(x-0.1)**2
a= 0
b = 0.256

m=np.arange(a,b,0.001)

plt.plot(m,f(m))

plt.plot(m,ft2(m))

plt.show()


