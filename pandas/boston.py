# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 08:49:35 2022

@author: DISRCT
"""

import pandas as pd

boston = pd.read_csv("data/BostonHousing.csv", sep=",")

print(boston.loc[:14, ["crim", "medv"]])