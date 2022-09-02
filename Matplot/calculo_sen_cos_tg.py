# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:10:57 2022

@author: disrct
"""

import math
import numpy as np
import matplotlib.pyplot as plt

lista = []

for i in range(100):
    lista.append(((6/100) * i) - 3)

xRange = np.array(lista)

array = np.arange(100)

seno = []
cosseno = []
tangente = []

for i in array:
    seno.append(math.sin(xRange[i]))
    cosseno.append(math.cos(xRange[i]))
    tangente.append(math.tan(xRange[i]))

array = np.linspace(-3, 3, 100)
seno = np.array(seno)
cosseno = np.array(cosseno)
tangente = np.array(tangente)

fig, eixo = plt.subplots(nrows = 1, ncols = 3, figsize = (60, 20))
eixo[0].plot(array, seno, color = 'red', linewidth = 3, label = 'Seno')
eixo[1].plot(array, cosseno, color = 'blue', linewidth = 3, label = 'Cosseno')
eixo[2].plot(array, tangente, color = 'blue', linewidth = 3, label = 'Tangente')

eixo[0].legend()
eixo[1].legend()
eixo[2].legend()

fig.savefig('Grafico.png')