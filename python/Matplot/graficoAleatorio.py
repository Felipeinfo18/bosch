# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:38:12 2022

@author: disrct
"""

import matplotlib.pyplot as plt
import numpy as np

# criação da distribuição de pontos
array = (np.random.rand(20) * 2) - 1
print(array)
tam = np.arange(20)


# gráfico de y em função de x
plt.rcParams["figure.figsize"] = (35, 25)
plt.rcParams.update({'font.size': 40})

plt.plot(tam, array, label = "Random Values", linewidth = 20)
plt.legend()
plt.axis([0, 20, -1.5, 1.5])

# cálculo da média e do desvio padrão com funções prontas do NumPy
media = np.array([np.mean(array)] * len(array))
dp = np.array([np.std(array)] * len(array))
plt.plot(tam, media - dp, color = 'blue', linestyle = 'dashed', linewidth = 9)
plt.plot(tam, media + dp, color = 'blue', linestyle = 'dashed', linewidth = 9)
plt.plot(tam, media, color = 'blue', linewidth = 9)
