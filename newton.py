import matplotlib.pyplot as plt
import math
import numpy as np
def f(x):
    return 73*math.e**(-1.5*x)+22*math.e**(-0.075*x)-14

def df(x):
    return -109.5*math.e**(-1.5*x)-1.65*math.e**(-0.075*x)

def newton(x0, Erro, itMax):
    it =0
    Er =1
    x =x0
    while(Er >= Erro and it<itMax):
        xold=x
        x = xold - f(xold)/df(xold)
        Er = np.abs((x-xold)/x)
        it = it+1
    return (x, Er, it)
x0=3
Erro = 10**-3
itMax=4
res = newton(x0, Erro, itMax)

print('O valor da raiz é:',res[0])
print('O valor do erro foi:',res[1])
print('O numero de iterações:',res[2])