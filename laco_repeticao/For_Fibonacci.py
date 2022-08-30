# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 09:05:33 2022

@author: disrct
"""

numero = int(input("Digite o número de fatores: "))
valor1 = 0
valor2 = 1
#variavel de armazenamento
guarda = 0

for i in range(0, numero):
    print(valor1)
    guarda = valor2
    valor2 += valor1
    valor1 = guarda