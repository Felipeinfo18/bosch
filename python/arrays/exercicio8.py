# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 09:18:00 2022

@author: DISRCT
"""

import numpy as np

def VerificaSimetria(matrizA):
    dimensions = np.shape(matrizA)
    
    if dimensions[0] == dimensions[1]:    
        for i in range(dimensions[0]):
            for l in range(dimensions[1]):
                if i != l:
                    if matrizA[i][l] != matrizA[l][i]:
                        return False
    else:
        return False
    
    return True

matrizA = np.array([2, -1, 5, -1, -3, 2, 5, 2, 8])
matrizA = matrizA.reshape(3, 3)

if np.array_equal(matrizA, matrizA.T):
    print("É simétrico!")
else:
    print("Não é simétrico!")
    
# =============================================================================
# if VerificaSimetria(matrizA):
#     print("É simétrico!")
# else:
#     print("Não é simétrico!")
# =============================================================================
