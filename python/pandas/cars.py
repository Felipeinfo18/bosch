# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 09:38:11 2022

@author: DISRCT
"""

import pandas as pd

df = pd.read_csv("data/Cars93_miss.csv", usecols=["Manufacturer", "Make", "Price", "MPG.city", "Type", "Passengers"])
df = df[df["Passengers"]==5].dropna()

df = df.sort_values("MPG.city", ascending = False).iloc[:10]

df = df.sort_values("Price").iloc[:5]
print(df)
