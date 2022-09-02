# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 10:13:46 2022

@author: disrct
"""

import matplotlib.pyplot as plt
import numpy as np

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# temperaturas máxima média e mínima média (em graus Celsius)
temp_max = [26.8,	26.8,	26,	24,	20.8,	20.1,	19.7, 21.5,	21.4,	23.1,	25,	26.2]
temp_min = [17.2,	17.4,	16.5,	14.6,	11.2,	9.7, 9, 9.6, 11.1,	13.2,	14.9,	16.2]
meses = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
fig1,ax1 = plt.subplots(figsize=(15, 5))

# continue a solução
plt.rcParams.update({'font.size': 14})
 
tam = np.arange(12)
help(plt.plot)
plt.plot(meses, temp_max, linewidth = 2, marker = 'o', markersize = 8, mfc = 'white', color = 'red', label = "Max temp")
plt.plot(meses, temp_min, linewidth = 2, marker = 'o', markersize = 8, mfc = 'white', color = 'blue', label = "Min temp")
plt.axis([0, 10, 0, 35])

ax1.set_xlabel("Meses")
ax1.set_ylabel("Temperatura")
fig1.legend(loc = 'upper right')

plt.grid(color='lightblue')
plt.fill_between(tam, temp_min, temp_max, color = '#F281B9')
plt.fill_between(tam, 0, temp_min, color = '#81EEF2')
