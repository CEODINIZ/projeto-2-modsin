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


lista_tempo= np.arange(0,84600,1e-2)

Potencia=[1200,1400,1600,1800,2000,2200,2400,2600,2800,3000,3200,3400,3600,3800]
Hs=60
As=2
To=25+273
Dp=0.1
Kp=0.17
Ap=1.6
Hp=0.03
M=1600
C=4186

for e in Potencia:

    solucao=odeint(equacaodiferencial_tempo,To,lista_tempo, args=(e,Hs,As,To,Dp,Kp,Ap,Hp,M,C,))


    plt.plot(lista_tempo,solucao)
plt.xlabel("Tempo(segundos)")
plt.ylabel("Temperatura(kelvin)")
plt.grid(True)
plt.show()




#Potencia,Hs,As,Tf,To,Dp,Kp,Ap,Hp,M,C,