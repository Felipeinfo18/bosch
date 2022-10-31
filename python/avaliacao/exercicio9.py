# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 09:14:02 2022

@author: DISRCT
"""

import numpy as np # Importa Numpy

array = np.random.randint(1, 10, (5,5)) # Cria uma matriz 5x5 com valores aleatórios

print('\n', array) # printa a matriz 5x5

condition = (array % 2 != 0) # Cria uma matriz booleana baseado nos valores impares da matriz 5x5 de mesmo tamanho
array[condition] = array[condition] ** 2 # Pega a matriz 5x5 e substitui todos os valores impares pelos valores correspondentes elevados ao quadrado

print('\n', array) # printa array com os valores atualizados