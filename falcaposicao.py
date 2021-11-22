import matplotlib.pyplot as plt
import math
import numpy as np



def f(x):
    return -3*x**(4)-4*x**(2)+5*x+6


def falsaposicao(a,b,Erro,itMax):
    it = 0
    x=a
    Er=1
    while(Er >=Erro and it<itMax):
        xold = x
        x = a-(f(a)*(b-a))/(f(b)-f(a))
        Er = np.abs((x-xold)/x)
        if(f(a)*f(x)<0):
            b=x
        else:
            a=x
        it=it+1
    return(x,Er,it)


a = 0
b = 2
Erro = 10**-10
itMax = 5

m=np.arange(a , b , 1)
plt.plot(m , f(m))
plt.show()
res = falsaposicao(a , b , Erro , itMax)

print('O valor da raiz é:',res[0])
print('O valor do erro foi:',res[1])
print('O numero de iterações:',res[2])