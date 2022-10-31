# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:24:43 2022

@author: DISRCT
"""

with open('teste.txt') as arquivo:
    for linha in arquivo:
        print(linha, end='')

if arquivo.closed: print("Encerrado!")
