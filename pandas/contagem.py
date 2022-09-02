# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:31:57 2022

@author: DISRCT
"""

import pandas as pd

def calculate_percentage(val, total):
    """Calculates the percentage of a value over a total"""

    percent = float(val / total)
    beautiful_percent = ("%.2f" % (percent * 100) + "%")
    return beautiful_percent

titanic = pd.read_csv("data/titanic.csv")

total = titanic.Survived.count()
mortos = titanic.Survived[titanic.Survived == 0].count()
sobreviventes = titanic.Survived[titanic.Survived == 1].count()

classe1 = titanic[titanic.Pclass == 1]
classe2 = titanic[titanic.Pclass == 2]
classe3 = titanic[titanic.Pclass == 3]


mortos_1classe = classe1.Survived[classe1.Survived == 0].count()
mortos_2classe = classe2.Survived[classe2.Survived == 0].count()
mortos_3classe = classe3.Survived[classe3.Survived == 0].count()

vivos_1classe = classe1.Survived[classe1.Survived == 1].count()
vivos_2classe = classe2.Survived[classe2.Survived == 1].count()
vivos_3classe = classe3.Survived[classe3.Survived == 1].count()

print(f"Não sobreviveu da primeira classe: {calculate_percentage(mortos_1classe, mortos)}")
print(f"Não sobreviveu da segunda classe: {calculate_percentage(mortos_2classe, mortos)}")
print(f"Não sobreviveu da terceira classe: {calculate_percentage(mortos_3classe, mortos)}")
print()
print(f"Sobreviveu da primeira classe: {calculate_percentage(vivos_1classe, sobreviventes)}")
print(f"Sobreviveu da segunda classe: {calculate_percentage(vivos_2classe, sobreviventes)}")
print(f"Sobreviveu da terceira classe: {calculate_percentage(vivos_3classe, sobreviventes)}")
