import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#primeiro codigo
#fazendo o gráfico pego na internet usando os pontos obtidos no Web Plot.

lista_pontos=[20.7+273,23.4+273,27+273,30.6+273,34.3+273,37+273,40.1+273,44.2+273,46.9+273]
#criando a lista tempo do Web Plot
tempo=[0,0.24,0.87,1.35,1.50,1.81,2.45,2.75,3.07]




#segundo código
#definindo a equação diferencial


def equacaodiferencial_tempo(Tf,t,Potencia,Hs,As,To,Dp,Kp,Ap,Hp,M,C):
    x= Potencia
    y= -Hs * As *(Tf-To)
    z= -((Tf-To)/((Dp/(Kp*Ap))+(1/(Hp*Ap))))
    w= M * C
    dTdt= (x+y+z)/w

    return dTdt
#criando a lista tempo

lista_tempo= np.arange(0,3,10**-2)
#definindo os valores
Potencia=270
Hs=60
As=0.003
To=20+273
Dp=0.001
Kp=0.17
Ap=0.005
Hp=0.03
M=0.720
C=41.86

#fazendo a solução usando o Odeint
solucao=odeint(equacaodiferencial_tempo,To,lista_tempo, args=(Potencia,Hs,As,To,Dp,Kp,Ap,Hp,M,C,))

#plotando o gráfico
plt.plot(lista_tempo,solucao,"g",label="Simulação do modelo")
plt.plot(tempo,lista_pontos,"r-", label="Gráfico da internet")
plt.xlabel("Tempo(minutos)")
plt.ylabel("Temperatura(kelvin)")
plt.legend()
plt.grid(True)
plt.show()

