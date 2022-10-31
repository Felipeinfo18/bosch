# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 08:13:58 2022

@author: DISRCT
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/respiradores.csv")
x = df.MES
altura = df.TOTAL
# =============================================================================
# 
# plt.barh(x, altura, color="purple")
# # =============================================================================
# # 
# # plt.bar(x, altura, .5, align="center", edgecolor = "black")
# plt.title("COMPRA DE RESPIRADORES POR MÊS")
# # plt.xticks(rotation = '90')
# # plt.yticks(rotation = '45')
# # =============================================================================
# plt.show()
# help(plt.bar)
# =============================================================================

# =============================================================================
# 
# plt.plot(df.MES,df.PARANA,marker='o', label = 'Paraná')
# plt.plot(df.MES,df['SÃO PAULO'],marker='o', label = 'São Paulo')
# plt.plot(df.MES,df['SANTA CATARINA'],marker='o', label = 'Santa Catarina')
# plt.legend()
# plt.xticks(rotation='45')
# plt.grid(linestyle='dashed')
# plt.show()
# =============================================================================

plt.scatter(df['MES'],df['PARANA'], label = 'Paraná')
plt.scatter(df['MES'],df['SANTA CATARINA'], label = 'Santa Catarina')
plt.scatter(df['MES'],df['GOIAS'], label = 'Goiás')
plt.scatter(df['MES'],df['PERNAMBUCO'], label = 'Pernambuco')
plt.scatter(df['MES'],df['AMAPA'], label = 'Amapá')
plt.legend() #fontsize=10 / prop={"size":10}
plt.title("")
plt.xticks(rotation=45)
plt.show()
help(plt.legend)