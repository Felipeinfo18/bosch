# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:10:27 2022

@author: DISRCT
"""


import numpy as np

def NegativoAleatorio(matriz):
    for i in range(len(matriz)):
        if np.random.randint(0, 2) == 1:
           matriz[i] = matriz[i] * -1

    return matriz

matriz1 = np.random.rand(36)
NegativoAleatorio(matriz1)
matriz1 = matriz1.reshape(6, 6)
matriz2 = np.random.rand(36)
NegativoAleatorio(matriz2)
matriz2 = matriz2.reshape(6, 6)


print(matriz1)
print(matriz2)
print(np.dot(matriz1, matriz2))