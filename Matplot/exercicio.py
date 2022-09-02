# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 09:31:50 2022

@author: DISRCT
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data/respiradores.csv")
norte = df.loc[:, ["AMAZONAS", "ACRE", "RONDONIA", "RORAIMA", "AMAPA", "PARA", "TOCANTINS"]]
nordeste = df.loc[:, ["MARANHÃO", "PIAUI", "RIO GRANDE DO NORTE", "CEARA", "PARAIBA", "BAHIA", "PERNAMBUCO", "ALAGOAS", "SERGIPE"]]
centroOeste = df.loc[:, ["GOIAS", "MATO GROSSO", "MATO GROSSO DO SUL", "DISTRITO FEDERAL"]]
sudeste = df.loc[:, ["MINAS GERAIS", "ESPIRITO SANTO", "RIO DE JANEIRO", "SÃO PAULO"]]
sul = df.loc[:, ["SANTA CATARINA", "PARANA", "RIO GRANDE DO SUL"]]

totalNorte =  norte.sum(axis=1)
totalNordeste = nordeste.sum(axis=1)
totalCentroOeste = centroOeste.sum(axis=1)
totalSudeste = sudeste.sum(axis=1)
totalSul = sul.sum(axis=1)
meses = df.MES
 
print(totalNorte)
# listaNomes = ["Norte", "Nordeste", "Centro Oeste", "Sudeste", "Sul"]
# listaTotais = [totalNorte, totalNordeste, totalCentroOeste, totalSudeste, totalSul]

# fig, eixo = plt.subplots(nrows = 1, ncols = 2, figsize = (20, 5))

plt.figure(figsize=(25,15))
plt.bar([i+0.2 for i in range(df.shape[0])], totalNorte, width = 0.15,
        label = 'Norte', align = 'edge')
plt.bar([i+0.4 for i in range(df.shape[0])], totalNordeste, width = .15,
        label = 'Nordeste', align = 'edge')
plt.bar([i+0.6 for i in range(df.shape[0])], totalCentroOeste, width = 0.15,
        label = 'Centro Oeste', align = 'edge')
plt.bar([i+.8 for i in range(df.shape[0])], totalSudeste, width = 0.15,
        label = 'Sudeste', align = 'edge')
plt.bar([i+1 for i in range(df.shape[0])], totalSul, width = 0.15,
        label = 'Sul', align = 'edge')

plt.xticks(np.arange(11), meses, rotation=45, fontsize = 30)
plt.legend(fontsize=40)

# eixo[0].bar([a+0.25 for a in range(df.shape[0])],df.TOTAL/30,width = -0.25,
#        label = 'Média brasileira', align = 'edge')

# p, tx, autotexts = eixo[1].pie(listaTotais, labels = listaNomes, autopct = "", shadow=True)

# for i, a in enumerate(autotexts):
#     a.set_text("{}".format(listaTotais[i]))
    

