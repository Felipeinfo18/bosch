# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:53:50 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

idadeMedia = titanic.Age.mean()

print(idadeMedia)

titanic.Age = titanic.Age.fillna(idadeMedia)
print(titanic.Age.head(20))
print(titanic.Age.isnull().sum())