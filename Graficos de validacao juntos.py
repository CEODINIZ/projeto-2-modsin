#codigo 1
import matplotlib.pyplot as plt

lista_pontos=[20.7+273,23.4+273,27+273,30.6+273,34.3+273,37+273,40.1+273,44.2+273,46.9+273]

tempo=[0,0.24,0.87,1.35,1.50,1.81,2.45,2.75,3.07]




#codigo 2

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def equacaodiferencial_tempo(Tf,t,Potencia,Hs,As,To,Dp,Kp,Ap,Hp,M,C):
    x= Potencia
    y= -Hs * As *(Tf-To)
    z= -((Tf-To)/((Dp/(Kp*Ap))+(1/(Hp*Ap))))
    w= M * C
    dTdt= (x+y+z)/w

    return dTdt


lista_tempo= np.arange(0,3,10**-2)

Potencia=300
Hs=60
As=0.003
To=20+273
Dp=0.001
Kp=0.17
Ap=0.005
Hp=0.03
M=0.720
C=41.86


solucao=odeint(equacaodiferencial_tempo,To,lista_tempo, args=(Potencia,Hs,As,To,Dp,Kp,Ap,Hp,M,C,))


plt.plot(lista_tempo,solucao)
plt.plot(tempo,lista_pontos,"ro")
plt.xlabel("Tempo(minutos)")
plt.ylabel("Temperatura(kelvin)")
plt.grid(True)
plt.show()

#Potencia,Hs,As,Tf,To,Dp,Kp,Ap,Hp,M,C,