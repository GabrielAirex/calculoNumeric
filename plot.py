import matplotlib.pyplot as plt

import numpy as np


//definição da função que será usada
def f(x):
    return 31-((9.8*x)/13)*(1.-np.exp(-6.0*(13.0/x)))
//Onde definiremos o tamanho do intervalo
a= 40
b = 140
// gera o vetor intervalo e o espaçamento
m=np.arange(a,b,1)
// faz o plot da função
plt.plot(m,f(m))
// chama o plot
plt.show()

