# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 08:24:09 2022

@author: DISRCT
"""

import numpy as np

# Array de 0 a 9
# =============================================================================
# array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 
# print(array)
# print(type(array))
# 
# =============================================================================

# Array de 0 a 100 de 10 em 10
# =============================================================================
# array = np.arange(0, 101, 10)
# 
# print(array)
# =============================================================================

# Array de 10 x 10 com True
# =============================================================================
# array = np.full((10, 10), True)
# 
# print(array)
# =============================================================================


# Comandos Array
# =============================================================================
# shape para retornar a dimensão do array
# reshape para alterar o shape
# max retorna o valor maximo do array
# min retorna o valor minimo do array
# mean retorna a media
# median retorna a mediana
# var retorna a variancia
# 
# =============================================================================

# Trabalhando com índices do Array
# =============================================================================
# [:3]
# [0, 2]
# [0][2]
# [:2, :2]
# [0:10:2]
# 
# =============================================================================

# Trabalhando com 2 arrays
# =============================================================================
# copy() para copiar o conteudo
# union1d() para juntar arrays sem valores repetidos
# intersect1d() para pegar valores em comum entre arrays
# unique() para pegar apenas valores sem serem repetidos
# setdiff1d() pega valores que tem em um array e nao tem em outro
# 
# =============================================================================

# Substituindo impares por 0 usando operações de array
# =============================================================================
# array = np.random.randint(0, 20, (3, 3))
# print(array)
# array[array % 2 != 0] = 0
# print(array)
# 
# =============================================================================

# Operações com Array
# =============================================================================
# array = np.random.randint(0, 50, (2, 3))
# 
# print(array)
# array = array.reshape(3, 2)
# print(array)
# array[0] += 5
# print(array)
# array[1] = array[1] * 3
# print(array)
# array[:,1] = array[:,1] / 2
# print(array)
# =============================================================================
