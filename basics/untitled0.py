# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 08:18:40 2022

@author: disrct
"""
lista = []

for i in range(10):
    lista.append(int(input(f"Valor {i+1}: ")))


print(f"TAMANHO DA LISTA: {len(lista)}")
print(sorted(lista))