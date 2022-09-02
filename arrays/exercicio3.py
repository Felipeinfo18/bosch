# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:07:48 2022

@author: DISRCT
"""

import numpy as np

matriz = np.random.randint(0, 100, 20)
matriz = matriz.reshape(4, 5)
print(matriz)
print(matriz.sum())