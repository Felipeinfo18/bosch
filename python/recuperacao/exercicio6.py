# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 09:59:53 2022

@author: disrct
"""

import pandas as pd
import matplotlib.pyplot as plt

superheroes = pd.read_csv("superheroes.csv").dropna()

indices = superheroes.groupby("creator").strength_score.mean().index
valores = superheroes.groupby("creator").strength_score.mean().values

plt.bar(indices, valores, color='black', zorder=5)
plt.xticks(rotation = 45)
plt.ylabel("Strength Mean")
plt.grid(zorder = 2)

imortais = superheroes[superheroes.has_immortality == True]

print("Os melhores imortais em combate são: ")
imortais = imortais.nlargest(5, 'combat_score')

for i in range(len(imortais)):
    print(f"{i+1} - {imortais.name.values[i]}")
    