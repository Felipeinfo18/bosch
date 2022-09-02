# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 08:24:50 2022

@author: DISRCT
"""

import numpy as np

def produtoMatricial(matriz1, matriz2):
    dimensions1 = np.shape(matriz1)
    dimensions2 = np.shape(matriz2)
    matrizC = np.zeros(dimensions1[0] * dimensions2[1])
    
    matrizC = matrizC.reshape(dimensions1[0], dimensions2[1])
    if dimensions1[1] == dimensions2[0]:
        for i in range(dimensions1[0]):
            for l in range(dimensions2[1]):
                for k in range(dimensions1[1]):
                    matrizC[i][l] += matriz1[i][k] * matriz2[k][l]
                    
                
    return matrizC
    
matriz1 = np.random.randint(0, 100, 20)
matriz1 = matriz1.reshape(4, 5)
matriz2 = np.random.randint(0, 100, 20)
matriz2 = matriz2.reshape(5, 4)
matrizC = produtoMatricial(matriz1, matriz2)
print(matrizC)
print(np.dot(matriz1, matriz2))