# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:47:25 2022

@author: DISRCT
"""

import numpy as np

array = np.random.randint(0, 10, 25)
array = array.reshape(5, 5)

print(array)

for i in range(5):
    for l in range(5):
        if array[i][l] % 2 != 0:
            array[i][l] = 0
            
print(array)