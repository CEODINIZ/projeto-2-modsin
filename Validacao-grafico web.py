


import matplotlib.pyplot as plt

lista_pontos=[20.7+273,23.4+273,27+273,30.6+273,34.3+273,37+273,40.1+273,44.2+273,46.9+273]

tempo=[0,0.24,0.87,1.35,1.50,1.81,2.45,2.75,3.07]



plt.plot(tempo,lista_pontos)
plt.xlabel("Tempo(minutos)")
plt.ylabel("Temperatura(kelvin)")
plt.grid(True)
plt.show()

