# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 11:03:20 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

titanic = titanic[(titanic["Embarked"] == 'S') & (titanic["Pclass"] == 2) & (titanic["Age"] == 29) & (titanic["Name"].str.contains("Anne"))]
print(titanic["Survived"].values[0])
print(f"A mulher que ele está procurando é {titanic.Name.values[0]}, ela sobreviveu")