import matplotlib.pyplot as plt
import math
import numpy as np
def f(x):
    return 85*x-85*x*(1.04)**(x)-18.24



def secante(x0,x1, Erro, itMax):
    it =0
    Er =1
    xa1=x0
    x=x1
    while(Er >= Erro and it<itMax):
        xa2 =xa1
        xa1 =x
        x = xa1 - (f(xa1)*(xa2-xa1))/(f(xa2) - f(xa1))
        Er = np.abs((x-xa1)/x)
        it = it+1
    return (x, Er, it)
x0=2
x1=-12
Erro = 10**(-0)
itMax=4
res = secante(x0,x1, Erro, itMax)

print('O valor da raiz é:',res[0])
print('O valor do erro foi:',res[1])
print('O numero de iterações:',res[2])