# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:10:45 2022

@author: DISRCT
"""

import numpy as np

def celsiusFahrenheit(array):
    dimensions = np.shape(array)
    fahrenheit = np.zeros(dimensions)
    for i in range(dimensions[0]):
        fahrenheit[i] = (array[i] * 1.8) + 32
    return fahrenheit

temperaturasCelsius = np.random.randint(10, 91, 20)

temperaturasFahrenheit = celsiusFahrenheit(temperaturasCelsius)

print(temperaturasCelsius)
print(temperaturasFahrenheit)