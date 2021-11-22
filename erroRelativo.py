import matplotlib.pyplot as plt
import math
import numpy as np

def precisao(x,xold):
    k = 1
    Er = np.abs((x - xold) / x)
    return (Er)

x=0.51747
xold=0.51671
res = precisao(x,xold)

print('O valor do erro foi:',res)



