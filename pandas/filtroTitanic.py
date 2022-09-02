# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:50:32 2022

@author: DISRCT
"""

import pandas as pd

titanic = pd.read_csv("data/titanic.csv").dropna()

print(titanic[((titanic["Pclass"] == 1) & (titanic["Survived"] == 1)) | ((titanic["Pclass"] == 3) & (titanic["Survived"] == 0))])