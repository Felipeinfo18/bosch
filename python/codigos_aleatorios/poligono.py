# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 09:32:21 2022

@author: disrct
"""

def calculaProd(ponto1, ponto2):
    valor1 = ponto1[0] * ponto2[1]
    valor2 = ponto1[1] * ponto2[0]
    return valor1 - valor2


def calculaPontos(ponto1):
    global poligono
    
    for i in range(len(poligono)):
        u = [(poligono[2-i][0] - poligono[1-i][0]), (poligono[2-i][1] - poligono[1-i][1])]
        v = [(ponto1[0] - poligono[2-i][0]), (ponto1[1] - poligono[2-i][1])]
        
        produto = calculaProd(u, v)    
        
        if produto < 0:
            return False

    return True
    

poligono = [(10,10), (5, 8), (3,5), (5, 0), (11, 1), (14, 6)]

while True:
    ponto = input("Insira o ponto (x, y): ").split()
    ponto = tuple([eval(i) for i in ponto])
    
    resultado = calculaPontos(ponto)
    
    if resultado == True:
        print(f"O ponto {ponto} está dentro do polígono!")
    else:
        print(f"O ponto {ponto} não está dentro do polígono!")

    if input("Deseja inserir outro ponto? (S/n) > ")[0].lower() == 'n':
        break