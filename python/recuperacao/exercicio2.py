# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 08:33:00 2022

@author: disrct
"""

import numpy as np

arr = np.random.randint(0, 10, (5,5))

cont = 0

for i in range(len(arr)):
    for l in range(len(arr[i])):
        if (arr[i][l] % 2 != 0):
            cont += 1

print(f"A array original: \n{arr}\n")
             
arr[arr % 2 != 0] = arr[arr % 2 != 0] ** 2

arquivo = open('arquivo.txt', 'r')
numero = int(arquivo.read())
arquivo.close()

arquivo = open('arquivo.txt', 'w')
arquivo.write(str(cont + numero))
arquivo.close()

print(f"A array substituindo os números ímpares: \n{arr}\n")
print(f"Existem {cont+numero} registros")
