import matplotlib.pyplot as plt
import math
import numpy as np



def f(x):
    return 31-((9.8*x)/13)*(1.-np.exp(-6.0*(13.0/x)))


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


a = 52
b = 55
Erro = 10**-4
itMax = 6

m=np.arange(a , b , 1)
n=np.arange(0,0,1)
plt.plot(m , f(m))
plt.show()
res = bisseccao(a , b , Erro , itMax)

print('O valor da raiz é:',res[0])
print('O valor do erro foi:',res[1])
print('O numero de iterações:',res[2])