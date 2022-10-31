# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 08:09:48 2022

@author: disrct
"""

import pandas as pd
import matplotlib.pyplot as plt

netflix = pd.read_csv("netflix_titles.csv").dropna()

# parte 1 do exercicio
# =============================================================================
# netflix = netflix[(netflix.country == "United States") & (netflix.release_year >= 2015) & (netflix.release_year <= 2020)]
# 
# plt.bar(2015, netflix[netflix.release_year == 2015].count())
# plt.bar(2016, netflix[netflix.release_year == 2016].count())
# plt.bar(2017, netflix[netflix.release_year == 2017].count())
# plt.bar(2018, netflix[netflix.release_year == 2018].count())
# plt.bar(2019, netflix[netflix.release_year == 2019].count())
# plt.bar(2020, netflix[netflix.release_year == 2020].count())
# 
# 
# =============================================================================

# parte 2 do exercicio
def filtraTempo(tempo):
    global tempos
    tempo = tempo.split()
    tempo = tempo[0]
    tempos.append(tempo)

def converteTempos():
    global tempos
    guarda = []
    for tempo in tempos:
        guarda.append(int(tempo))
    return guarda

def maisLongos():
    global tempos
    tempos = converteTempos()
    maisLongos = []
    for i in range(5):
        tempo = max(tempos)
        tempos.remove(tempo)
        maisLongos.append(tempo)
    return maisLongos

tempos = []

netflix = netflix[(netflix.country == "Brazil") & (netflix.type == "Movie")]
netflix.duration.apply(filtraTempo)

filmes = []
tempos = maisLongos()

for i in range(5):
    filmes.append(netflix.title[(netflix.duration == str(tempos[i]) + " min")])
    
for i in range(5):
    print(f"filme: {filmes[i].values} duração: {tempos[i]}")