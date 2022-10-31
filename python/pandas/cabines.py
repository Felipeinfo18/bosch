# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:15:52 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")
# filtro = titanic.groupby("Cabin")["PassengerId"].count()
print(titanic.groupby("Cabin").Cabin.count())