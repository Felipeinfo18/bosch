# -*- cod/,ng: utf-8 -*-
"""
Created on Wed Aug 24 11:40:28 2022

@author: DISRCT
"""

palavra = input("Escolha uma palavra: ").lower()
quantidade = 0

with open('arquivo.txt') as arquivo:
    for linha in arquivo:
        if linha != '\n': 
            palavras = linha.split(" ")
            palavras = palavras[0].strip().lower()
            if palavra == palavras: quantidade += 1

print(f"A palavra se repetiu {quantidade} vezes")   