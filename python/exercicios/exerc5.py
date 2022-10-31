# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:16:44 2022

@author: DISRCT
"""

pessoas = {}

for i in range(5):
    pessoa = []
    pessoa.append(input("Nome: "))
    pessoa.append(input("Altura: "))
    pessoas.update({i : pessoa})

maior = pessoas.get(0)[1]
menor = pessoas.get(0)[1]
nomeMaior = pessoas.get(0)[0]
nomeMenor = pessoas.get(0)[0]

for i in range(len(pessoas)):
    if pessoas.get(i)[1] > maior:
        maior = pessoas.get(i)[1]
        nomeMaior = pessoas.get(i)[0]

    if pessoas.get(i)[1] < menor:
        menor = pessoas.get(i)[1]
        nomeMenor = pessoas.get(i)[0]

print(f"A pessoa mais alta é {nomeMaior}")
print(f"A pessoa mais baixa é {nomeMenor}")
