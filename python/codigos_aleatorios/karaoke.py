# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 08:48:46 2022

@author: disrct
"""
import random

arquivo = open("musica.txt", 'r')

estrofeQtd = 0
estrofe = []
secretos = []

for linha in arquivo.readlines():
    palavras = linha.split()
    aleatorio = random.randint(0, len(palavras)-1)
    for i in range(len(palavras)):
        if i == aleatorio:
            palavras[i] = "_ " * len(palavras[i])
            secretos.append(palavras[i])
    estrofe.append(palavras)
    
    estrofeQtd += 1
    if estrofeQtd == 4:
        chutes = 0
        for i in range(4):
            print()
            for i in range(len(estrofe)):
                for l in range(len(estrofe[i])):
                    print(estrofe[i][l], end="")
                    print(" ", end="")
                print()
        
            chute = input(f"{chutes+1} > ")
            
            if chute == secretos[chutes]:
                
            
        secretos = []
        estrofeQtd = 0
        estrofe = []
        chutes += 1