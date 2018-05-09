

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
#equacao diferencial
def equacaodiferencial_tempo(Tf,t,Potencia,Hs,As,To,Dp,Kp,Ap,Hp,M,C):
    x= Potencia
    y= -Hs * As *(Tf-To)
    z= -((Tf-To)/((Dp/(Kp*Ap))+(1/(Hp*Ap))))
    w= M * C
    dTdt= (x+y+z)/w

    return dTdt
#fazendo a lista_tempo

lista_tempo= np.arange(0,84600,1e-2)
#definindo os parâmetros
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
#gerando as soluções pra cada potência e plotando os gráficos
for e in Potencia:

    solucao=odeint(equacaodiferencial_tempo,To,lista_tempo, args=(e,Hs,As,To,Dp,Kp,Ap,Hp,M,C,))


    plt.plot(lista_tempo,solucao,label= e)
plt.xlabel("Tempo(segundos)")
plt.ylabel("Temperatura(kelvin)")
plt.legend()
plt.grid(True)
plt.show()




