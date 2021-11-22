import matplotlib.pyplot as plt
import math
import numpy as np



def f(x):
    return 10.0*np.sin(x)*math.e**-(x)-1


def bisseccao(a,b,Erro,itMax):
    it = 0
    x=a
    Er=1
    while(Er >=Erro and it<itMax):
        xold = x
        x = (a+b)/2
        Er = np.abs((x-xold)/x)
        if(f(a)*f(x)<0):
            b=x
        else:
            a=x
        it=it+1
    return(x,Er,it)


a = 0.05
b = 0.15
Erro = 10**-10
itMax = 4

m=np.arange(a , b , 1)
n=np.arange(0,0,1)
plt.plot(m , f(m))
plt.show()
res = bisseccao(a , b , Erro , itMax)

print('O valor da raiz é:',res[0])
print('O valor do erro foi:',res[1])
print('O numero de iterações:',res[2])