# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:29:45 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

idade_por_sexo = titanic.groupby("Sex")["Age"].mean()
print(idade_por_sexo)