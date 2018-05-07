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


lista_tempo= np.arange(0,86400*2,1e-2)



Potencia=2000
Hs=60
As=2
To=25+273
Dp=0.1
Kp=0.17
Ap=1.6
Hp=0.03
M=1600
C=4186


solucao=odeint(equacaodiferencial_tempo,To,lista_tempo, args=(Potencia,Hs,As,To,Dp,Kp,Ap,Hp,M,C,))


plt.plot(lista_tempo,solucao)
plt.xlabel("Tempo(segundos)")
plt.ylabel("Temperatura(kelvin)")
plt.grid(True)
plt.show()

#Potencia,Hs,As,Tf,To,Dp,Kp,Ap,Hp,M,C,